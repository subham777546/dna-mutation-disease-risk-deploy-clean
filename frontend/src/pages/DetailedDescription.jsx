import { useNavigate } from "react-router-dom";
import "./DetailedDescription.css";

// Image imports (CORRECT WAY FOR VITE)
import dnaHelix from "../assets/details/dna_double_helix.png";
import karyotype from "../assets/details/human_karyotype.png";
import mitochondrial from "../assets/details/mitochondrial_dna.png";
import refAlt from "../assets/details/reference_vs_alternate.png";
import insDel from "../assets/details/insertion_deletion.png";
import frameshift from "../assets/details/frameshift_mutation.png";
import genomicPos from "../assets/details/genomic_position.png";

function DetailedDescription() {
  const navigate = useNavigate();

  return (
    <div className="details-page">
      {/* BACK BUTTON */}
      <button className="back-btn" onClick={() => navigate("/")}>
        ← Back to Predictor
      </button>

      <h1>Understanding DNA Mutations and Genomic Inputs</h1>

      {/* SECTION 1 */}
      <section>
        <h2>1. What is DNA?</h2>
        <p>
          DNA (Deoxyribonucleic Acid) is the fundamental molecule that carries
          genetic information in all living organisms. It contains the
          instructions required for growth, development, and normal functioning
          of cells.
        </p>
        <p>
          DNA has a double-helix structure, often described as a twisted ladder.
          The sides of the ladder are made of sugar and phosphate molecules, while
          the rungs are formed by pairs of chemical bases.
        </p>
        <ul>
          <li>A – Adenine</li>
          <li>T – Thymine</li>
          <li>G – Guanine</li>
          <li>C – Cytosine</li>
        </ul>
        <p>
          These bases pair specifically: A pairs with T, and G pairs with C.
        </p>

        <img src={dnaHelix} alt="DNA Double Helix" />
      </section>

      {/* SECTION 2 */}
      <section>
        <h2>2. What is a Chromosome?</h2>
        <p>
          DNA molecules are extremely long, so they are tightly packed into
          structures called chromosomes. Each chromosome contains a single long
          DNA molecule along with associated proteins.
        </p>
        <p>
          Humans have 23 pairs of chromosomes:
        </p>
        <ul>
          <li>Chromosomes 1–22 are autosomes</li>
          <li>X and Y are sex chromosomes</li>
        </ul>

        <img src={karyotype} alt="Human Chromosome Karyotype" />
      </section>

      {/* SECTION 3 */}
      <section>
        <h2>3. Chromosomes 1–22, X, Y, and MT</h2>
        <p>
          Genetic mutations are identified by the chromosome on which they occur.
          Chromosomes 1–22 contain most human genes.
        </p>
        <p>
          MT refers to mitochondrial DNA, which is inherited only from the
          mother and is responsible for cellular energy production.
        </p>

        <img src={mitochondrial} alt="Mitochondrial DNA" />
      </section>

      {/* SECTION 4 */}
      <section>
        <h2>4. What is a Reference Allele?</h2>
        <p>
          A reference allele is the DNA base or sequence considered standard at a
          specific genomic position, derived from the reference human genome.
        </p>
        <ul>
          <li>Reference Allele: A</li>
          <li>Most individuals carry this base</li>
        </ul>

        <img src={refAlt} alt="Reference vs Alternate Allele" />
      </section>

      {/* SECTION 5 */}
      <section>
        <h2>5. What is an Alternate Allele?</h2>
        <p>
          An alternate allele represents a variation from the reference allele
          caused by a mutation.
        </p>
        <ul>
          <li>Substitution (A → T)</li>
          <li>Insertion (A → ATG)</li>
          <li>Deletion (AT → A)</li>
        </ul>

        <img src={insDel} alt="Insertion and Deletion Mutation" />
      </section>

      {/* SECTION 6 */}
      <section>
        <h2>6. What Does “A → TTT” Mean?</h2>
        <p>
          This mutation replaces a single base with three bases, changing the
          length of the DNA sequence. Such mutations may disrupt protein
          synthesis and are often associated with higher disease risk.
        </p>

        <img src={frameshift} alt="Frameshift Mutation" />
      </section>

      {/* SECTION 7 */}
      <section>
        <h2>7. What is Genomic Position?</h2>
        <p>
          The genomic position specifies the exact base-pair location of a
          mutation on a chromosome.
        </p>
        <ul>
          <li>Chromosome: 17</li>
          <li>Position: 43,071,077</li>
        </ul>

        <img src={genomicPos} alt="Genomic Position Diagram" />
      </section>

      <footer>
        <p>
          Disclaimer: This content is for educational and research purposes only
          and does not constitute medical advice.
        </p>
      </footer>
    </div>
  );
}

export default DetailedDescription;
