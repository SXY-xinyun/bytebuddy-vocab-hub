# -*- coding: utf-8 -*-
extra = [
    ("prog-variable", "variable", "Programming", "noun", "/?ve?ri?bl/", "A named storage location in a program that holds a value which can change during execution.", "????????????????????????", "Declare the variable before the loop starts.", "Cambridge University Press. (2026). Variable. In Cambridge Dictionary."),
    ("prog-function", "function", "Programming", "noun", "/?f??k?n/", "A reusable block of code that performs a specific task when called.", "?????????????????????", "We wrote a function to sort the input array.", "Mozilla. (2026). Function. In MDN Web Docs."),
    ("prog-loop", "loop", "Programming", "noun", "/lu?p/", "A control structure that repeats a block of code while a condition is met.", "????????????????????????", "The loop printed each element in the list.", "Cambridge University Press. (2026). Loop. In Cambridge Dictionary."),
    ("prog-compile", "compile", "Programming", "verb", "/k?m?pa?l/", "To translate source code written in a high-level language into machine code or bytecode.", "??????????????????????", "The project failed to compile because of a type error.", "Oracle. (2026). Compile. In Java SE Documentation glossary."),
    ("prog-recursion", "recursion", "Programming", "noun", "/r??k???n/", "A technique where a function calls itself to solve a smaller instance of the same problem.", "????????????????????????", "Recursion needs a base case to stop infinite calls.", "Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to algorithms (4th ed.). MIT Press."),
    ("prog-iteration", "iteration", "Programming", "noun", "/??t??re??n/", "One repetition of a loop or the process of repeating steps until a goal is reached.", "??????????????????????????", "Each iteration updates the counter by one.", "IEEE. (2023). Iteration. In IEEE Software glossary."),
    ("prog-pointer", "pointer", "Programming", "noun", "/?p??nt?(r)/", "A value that stores the memory address of another value or object.", "???????????????????", "A null pointer caused the program to crash.", "ISO/IEC. (2018). ISO/IEC 9899:2018 (C standard) � pointer terminology."),
    ("prog-exception", "exception", "Programming", "noun", "/?k?sep?n/", "An event that disrupts normal program flow, often handled by catch blocks.", "??????????????????? catch ????", "Divide-by-zero raised an exception during the lab test.", "Oracle. (2026). Exceptions. In Java Tutorials."),
    ("prog-oop", "object-oriented programming", "Programming", "noun", "/??bd?ekt ??ri?ent?d ?pr???r�m??/", "A programming paradigm based on objects that combine data and behaviour.", "???????????????????????????????", "Object-oriented programming helps us model real-world entities.", "IBM. (n.d.). Object-oriented programming. In IBM Topics."),
    ("prog-compiler", "compiler", "Programming", "noun", "/k?m?pa?l?(r)/", "A program that translates entire source code into executable machine code before running.", "???????????????????????????", "The compiler reported two warnings and one error.", "Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2007). Compilers (2nd ed.). Pearson."),
    ("ai-training", "training", "AI & ML", "noun", "/?tre?n??/", "The process of adjusting model parameters using labelled or unlabelled data.", "????????????????????????", "Training stopped early because validation loss increased.", "Google. (n.d.). Training. In Google AI Glossary."),
    ("ai-overfitting", "overfitting", "AI & ML", "noun", "/???v??f?t??/", "When a model learns noise in training data and performs poorly on new data.", "???????????????????????????", "Dropout helped reduce overfitting on the small dataset.", "Google. (n.d.). Overfitting. In Google AI Glossary."),
    ("ai-feature", "feature", "AI & ML", "noun", "/?fi?t??(r)/", "An individual measurable property of the data used as input to a model.", "???????????????????", "We normalised each numeric feature before training.", "James, G., et al. (2021). An introduction to statistical learning (2nd ed.). Springer."),
    ("ai-classification", "classification", "AI & ML", "noun", "/?kl�s?f??ke??n/", "A supervised task of assigning inputs to discrete categories or classes.", "????????????????????????", "Email spam detection is a binary classification problem.", "Google. (n.d.). Classification. In Google AI Glossary."),
    ("ai-regression", "regression", "AI & ML", "noun", "/r???re?n/", "A supervised task of predicting a continuous numerical output.", "???????????????????", "Linear regression fit a line to the scatter plot.", "Google. (n.d.). Regression. In Google AI Glossary."),
    ("ai-epoch", "epoch", "AI & ML", "noun", "/?i?p?k/", "One complete pass through the entire training dataset during model training.", "?????????????????????", "The model converged after twenty epochs.", "PyTorch Foundation. (2026). Epoch. In PyTorch documentation."),
    ("ai-hyperparameter", "hyperparameter", "AI & ML", "noun", "/?ha?p?p??r�m?t?(r)/", "A configuration set before training, such as learning rate or batch size.", "??????????????????????", "We tuned the hyperparameter grid on a validation set.", "Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep learning. MIT Press."),
    ("ai-label", "label", "AI & ML", "noun", "/?le?bl/", "The correct output or category associated with a training example.", "???????????????????", "Volunteers checked each image label for mistakes.", "Google. (n.d.). Label. In Google AI Glossary."),
    ("ai-gradient", "gradient", "AI & ML", "noun", "/??re?di?nt/", "The vector of partial derivatives used to update weights during optimisation.", "?????????????????????", "The gradient vanished in the deepest layers.", "Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep learning. MIT Press."),
    ("ai-transformer", "transformer", "AI & ML", "noun", "/tr�ns?f??m?(r)/", "A neural architecture using self-attention to model relationships in sequences.", "Transformer?????????????????????", "Modern language models rely on the transformer architecture.", "Vaswani, A., et al. (2017). Attention is all you need. NeurIPS, 30."),
    ("math-vector", "vector", "Maths & Logic", "noun", "/?vekt?(r)/", "An ordered list of numbers representing magnitude and direction in space.", "???????????????????", "Add the two vectors component-wise in the exercise.", "Strang, G. (2016). Introduction to linear algebra (5th ed.). Wellesley-Cambridge Press."),
    ("math-logarithm", "logarithm", "Maths & Logic", "noun", "/?l???r?�?m/", "The exponent to which a base must be raised to produce a given number.", "??????????????????", "Logarithms turn multiplication into addition in complexity analysis.", "Stewart, J. (2015). Calculus (8th ed.). Cengage Learning."),
    ("math-derivative", "derivative", "Maths & Logic", "noun", "/d??r?v?t?v/", "The rate at which a function changes with respect to its input variable.", "??????????????????", "The derivative of x squared is two x.", "Stewart, J. (2015). Calculus (8th ed.). Cengage Learning."),
    ("math-integral", "integral", "Maths & Logic", "noun", "/??nt??r?l/", "A mathematical object representing area under a curve or accumulation of a quantity.", "??????????????????????", "We approximated the integral using rectangles.", "Stewart, J. (2015). Calculus (8th ed.). Cengage Learning."),
    ("math-permutation", "permutation", "Maths & Logic", "noun", "/?p??mju?te??n/", "An ordered arrangement of objects selected from a set.", "?????????????????", "Count permutations when order matters in passwords.", "Rosen, K. H. (2019). Discrete mathematics (8th ed.). McGraw-Hill."),
    ("math-proposition", "proposition", "Maths & Logic", "noun", "/?pr?p??z??n/", "A statement that is either true or false, but not both.", "???????????", "Write the proposition in symbolic logic notation.", "Rosen, K. H. (2019). Discrete mathematics (8th ed.). McGraw-Hill."),
    ("math-set", "set", "Maths & Logic", "noun", "/set/", "A collection of distinct elements considered as an object in mathematics.", "??????????????????", "The union of two sets includes all elements from both.", "Rosen, K. H. (2019). Discrete mathematics (8th ed.). McGraw-Hill."),
    ("math-eigenvalue", "eigenvalue", "Maths & Logic", "noun", "/?a???n?v�lju?/", "A scalar factor by which an eigenvector is scaled during a linear transformation.", "??????????????????????", "Eigenvalues appear in principal component analysis.", "Strang, G. (2016). Introduction to linear algebra (5th ed.). Wellesley-Cambridge Press."),
    ("math-combinatorics", "combinatorics", "Maths & Logic", "noun", "/?k?mb?n??t?r?ks/", "The branch of mathematics concerned with counting, arrangement and selection.", "?????????????????????", "Combinatorics explains why the password space is huge.", "Rosen, K. H. (2019). Discrete mathematics (8th ed.). McGraw-Hill."),
    ("math-linear-algebra", "linear algebra", "Maths & Logic", "noun", "/?l?ni?r ?�ld??br?/", "The study of vectors, matrices and linear transformations.", "?????????????????????", "Linear algebra underpins graphics and machine learning.", "Strang, G. (2016). Introduction to linear algebra (5th ed.). Wellesley-Cambridge Press."),
    ("lab-ide", "IDE", "Lab & Tools", "noun", "/?a? di? ?i?/", "Integrated Development Environment � software combining editor, debugger and build tools.", "?????????????????????????", "Open the IDE and run the unit tests.", "JetBrains. (2026). IDE. In JetBrains glossary."),
    ("lab-deployment", "deployment", "Lab & Tools", "noun", "/d??pl??m?nt/", "The process of making software available for use in a target environment.", "??????????????????", "Continuous deployment pushed the fix to production.", "GitLab. (2026). Deployment. In GitLab documentation."),
    ("lab-framework", "framework", "Lab & Tools", "noun", "/?fre?mw??k/", "A reusable software platform that provides structure and common functionality.", "?????????????????????", "The web framework handled routing and templates.", "Mozilla. (2026). Framework. In MDN Web Docs."),
    ("lab-version-control", "version control", "Lab & Tools", "noun", "/?v???n k?n?tr??l/", "A system that records changes to files so previous versions can be recovered.", "???????????????????????", "Version control saved us when the refactor broke tests.", "GitHub. (2026). About version control. In GitHub Docs."),
    ("lab-commit", "commit", "Lab & Tools", "noun", "/k??m?t/", "A snapshot of changes saved to a version control repository with a message.", "???????????????????????", "Write a clear commit message for each logical change.", "GitHub. (2026). About commits. In GitHub Docs."),
    ("lab-merge", "merge", "Lab & Tools", "verb", "/m??d?/", "To combine changes from different branches into one line of development.", "?????????????????????", "Resolve conflicts before you merge the feature branch.", "GitHub. (2026). Merging branches. In GitHub Docs."),
    ("lab-localhost", "localhost", "Lab & Tools", "noun", "/?l??k?l?h??st/", "The local computer used as a network host, often accessed via 127.0.0.1 during development.", "??????????? 127.0.0.1 ??????", "Run the server on localhost port 8080.", "Mozilla. (2026). localhost. In MDN Web Docs."),
    ("lab-debugger", "debugger", "Lab & Tools", "noun", "/di??b???(r)/", "A tool for executing code step by step and inspecting variables.", "???????????????????", "Set a breakpoint in the debugger on line ten.", "Microsoft. (2026). Debugger. In Visual Studio documentation."),
    ("lab-cloud", "cloud computing", "Lab & Tools", "noun", "/kla?d k?m?pju?t??/", "Delivery of computing services over the internet on a pay-as-you-go basis.", "?????????????????????", "We stored datasets in cloud storage for the group project.", "NIST. (2011). The NIST definition of cloud computing (SP 800-145). U.S. Department of Commerce."),
    ("lab-container", "container", "Lab & Tools", "noun", "/k?n?te?n?(r)/", "A lightweight package that includes code and dependencies for consistent runs.", "??????????????????????", "The container ran the same on every lab machine.", "Docker, Inc. (2026). What is a container? In Docker documentation."),
]

def js_entry(t):
    id_, w, m, pos, ph, en, zh, ex, src = t
    def q(s):
        return s.replace("\\", "\\\\").replace('"', '\\"')
    return f"""  {{
    id: "{q(id_)}",
    word: "{q(w)}",
    module: "{q(m)}",
    pos: "{q(pos)}",
    phonetic: "{q(ph)}",
    en_definition: "{q(en)}",
    zh_meaning: "{q(zh)}",
    example: "{q(ex)}",
    review_status: "New",
    date_added: "2026-10-23",
    source_apa: "{q(src)}",
  }}"""

if __name__ == "__main__":
    import pathlib
    out = ",\n".join(js_entry(t) for t in extra)
    pathlib.Path(__file__).resolve().parent.parent.joinpath("website/js/vocab-extra.js").write_text(
        "const VOCABULARY_EXTRA = [\n" + out + "\n];\n", encoding="utf-8"
    )
    print("wrote", len(extra), "entries")
