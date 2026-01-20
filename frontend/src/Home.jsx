import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import dnaImage from "./assets/dna.png";
import "./App.css";

function Home() {
  const navigate = useNavigate();

  const [chromosome, setChromosome] = useState("1");
  const [ref, setRef] = useState("");
  const [alt, setAlt] = useState("");
  const [position, setPosition] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    setLoading(true);
    setResult(null);

    try {
      const response = await axios.post("http://127.0.0.1:5000/predict", {
        chromosome,
        ref,
        alt,
        position
      });
      setResult(response.data);
    } catch {
      alert("Prediction failed. Check backend.");
    }

    setLoading(false);
  };

  return (
    <div className="page">
      {/* LEFT: PREDICTOR */}
      <div className="container">
        <h1>DNA Mutation Disease Risk Predictor</h1>

        <div className="form">
          <label>Chromosome</label>
          <select
            value={chromosome}
            onChange={(e) => setChromosome(e.target.value)}
          >
            {[...Array(22)].map((_, i) => (
              <option key={i + 1} value={i + 1}>
                {i + 1}
              </option>
            ))}
            <option value="X">X</option>
            <option value="Y">Y</option>
            <option value="MT">MT</option>
          </select>

          <label>Reference Allele</label>
          <input
            value={ref}
            onChange={(e) => setRef(e.target.value)}
            placeholder="e.g. A"
          />

          <label>Alternate Allele</label>
          <input
            value={alt}
            onChange={(e) => setAlt(e.target.value)}
            placeholder="e.g. TTT"
          />

          <label>Genomic Position</label>
          <input
            type="number"
            value={position}
            onChange={(e) => setPosition(e.target.value)}
            placeholder="e.g. 43071077"
          />

          <button onClick={handlePredict} disabled={loading}>
            {loading ? "Predicting..." : "Predict Risk"}
          </button>
        </div>

        {result && (
          <div
            className={`result ${
              result.prediction === "Likely Pathogenic"
                ? "pathogenic"
                : "benign"
            }`}
          >
            <h2>Prediction Result</h2>
            <p>
              <strong>Risk Probability:</strong> {result.risk_probability}
            </p>
            <p>
              <strong>Prediction:</strong>{" "}
              <span
                className={
                  result.prediction === "Likely Pathogenic"
                    ? "label-pathogenic"
                    : "label-benign"
                }
              >
                {result.prediction}
              </span>
            </p>
          </div>
        )}
      </div>

      {/* RIGHT: INFORMATION PANEL */}
      <div className="info-panel">
        <h2>How to Fill the Inputs</h2>

        <p>
          This tool predicts whether a genetic mutation is likely to be
          disease-causing based on historical clinical variant data.
        </p>

        <ul>
          <li>
            <strong>Chromosome:</strong> 1–22, X, Y, or MT (mitochondrial DNA)
          </li>
          <li>
            <strong>Reference Allele:</strong> Original DNA base(s) at that
            position
          </li>
          <li>
            <strong>Alternate Allele:</strong> Mutated base(s) replacing the
            reference
          </li>
          <li>
            <strong>Genomic Position:</strong> Exact DNA coordinate on the
            chromosome
          </li>
        </ul>

        <img src={dnaImage} alt="DNA Structure" className="dna-image" />

        <p>
          Example: If the reference allele is <strong>A</strong> and the
          alternate allele is <strong>TTT</strong>, this indicates a
          length-altering mutation which may increase disease risk.
        </p>

        {/* ✅ CONNECTED BUTTON */}
        <button
          className="details-btn"
          onClick={() => navigate("/details")}
        >
          Detailed Description
        </button>
      </div>
    </div>
  );
}

export default Home;
