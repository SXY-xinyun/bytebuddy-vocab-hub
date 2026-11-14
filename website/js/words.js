/**
 * Vocabulary database — one English word per entry (no abbreviations, no phrases).
 */
const VOCABULARY = [
  {
    id: "prog-algorithm",
    word: "algorithm",
    module: "Programming",
    pos: "noun",
    phonetic: "/ˈælɡərɪðəm/",
    en_definition:
      "A step-by-step procedure or set of rules designed to solve a problem or perform a computation.",
    zh_meaning: "算法；为解决某个问题或完成计算而设计的一步步规则或流程。",
    example: "Before coding, we drew the algorithm on paper to check the logic.",
    review_status: "New",
    source_apa: "Merriam-Webster. (n.d.). Algorithm. In Merriam-Webster.com dictionary. https://www.merriam-webster.com/dictionary/algorithm",
  },
  {
    id: "prog-debug",
    word: "debug",
    module: "Programming",
    pos: "verb",
    phonetic: "/diːˈbʌɡ/",
    en_definition: "To find and remove errors in computer code or a system.",
    zh_meaning: "调试；在程序或系统中查找并修复错误。",
    example: "She spent an hour debugging the loop that never terminated.",
    review_status: "New",
    source_apa: "Oxford University Press. (2026). Debug. In Oxford Learner's Dictionaries. https://www.oxfordlearnersdictionaries.com/definition/english/debug_1",
  },
  {
    id: "prog-syntax",
    word: "syntax",
    module: "Programming",
    pos: "noun",
    phonetic: "/ˈsɪntæks/",
    en_definition:
      "The set of rules that defines valid symbol combinations in a programming language.",
    zh_meaning: "语法；规定编程语言中哪些符号组合合法的一套规则。",
    example: "A missing semicolon caused a syntax error in his first C program.",
    review_status: "New",
    source_apa: "Cambridge University Press. (2026). Syntax. In Cambridge Dictionary. https://dictionary.cambridge.org/dictionary/english/syntax",
  },
  {
    id: "ai-dataset",
    word: "dataset",
    module: "AI & ML",
    pos: "noun",
    phonetic: "/ˈdeɪtəset/",
    en_definition:
      "A structured collection of data used for analysis, training, or testing models.",
    zh_meaning: "数据集；用于分析、训练或测试模型的结构化数据集合。",
    example: "The team cleaned the dataset before training the classifier.",
    review_status: "New",
    source_apa: "Google. (n.d.). Dataset. In Google for Developers machine learning glossary. https://developers.google.com/machine-learning/glossary",
  },
  {
    id: "ai-inference",
    word: "inference",
    module: "AI & ML",
    pos: "noun",
    phonetic: "/ˈɪnfərəns/",
    en_definition:
      "The process of using a trained model to make predictions on new data.",
    zh_meaning: "推理；用已训练好的模型对新的数据进行预测的过程。",
    example: "Inference on edge devices must be fast and energy-efficient.",
    review_status: "New",
    source_apa: "Google. (n.d.). Inference. In Google for Developers machine learning glossary. https://developers.google.com/machine-learning/glossary",
  },
  {
    id: "ai-perceptron",
    word: "perceptron",
    module: "AI & ML",
    pos: "noun",
    phonetic: "/pəˈseptrən/",
    en_definition:
      "A simple neural unit or model that learns a linear decision boundary.",
    zh_meaning: "感知机；一种学习线性决策边界的简单神经网络单元。",
    example: "The lecture introduced a perceptron for digit recognition.",
    review_status: "New",
    source_apa: "Rosenblatt, F. (1958). The perceptron: A probabilistic model for information storage and organization in the brain. Psychological Review, 65(6), 386–408. https://doi.org/10.1037/h0042519",
  },
  {
    id: "math-matrix",
    word: "matrix",
    module: "Maths & Logic",
    pos: "noun",
    phonetic: "/ˈmeɪtrɪks/",
    en_definition:
      "A rectangular array of numbers or symbols arranged in rows and columns.",
    zh_meaning: "矩阵；按行和列排列的数字或符号构成的矩形数组。",
    example: "Matrix multiplication is central to many graphics and ML formulas.",
    review_status: "New",
    source_apa: "Strang, G. (2016). Introduction to linear algebra (5th ed.). Wellesley-Cambridge Press.",
  },
  {
    id: "math-boolean",
    word: "boolean",
    module: "Maths & Logic",
    pos: "adjective",
    phonetic: "/ˈbuːliən/",
    en_definition:
      "Relating to a logical system with only two values, typically true and false.",
    zh_meaning: "布尔（的）；指只有真、假两种取值的逻辑体系。",
    example: "Boolean conditions control which branch of the program runs.",
    review_status: "New",
    source_apa: "Cambridge University Press. (2026). Boolean. In Cambridge Dictionary. https://dictionary.cambridge.org/dictionary/english/boolean",
  },
  {
    id: "math-proof",
    word: "proof",
    module: "Maths & Logic",
    pos: "noun",
    phonetic: "/pruːf/",
    en_definition:
      "A logical argument that demonstrates a statement is true under given assumptions.",
    zh_meaning: "证明；在给定假设下说明某命题为真的逻辑论证。",
    example: "The tutorial asked us to write a proof by induction.",
    review_status: "New",
    source_apa: "Cambridge University Press. (2026). Proof. In Cambridge Dictionary. https://dictionary.cambridge.org/dictionary/english/proof",
  },
  {
    id: "lab-terminal",
    word: "terminal",
    module: "Lab & Tools",
    pos: "noun",
    phonetic: "/ˈtɜːmɪnl/",
    en_definition:
      "A text-based interface where users type commands to interact with the operating system.",
    zh_meaning: "终端；通过输入命令与操作系统交互的文本界面。",
    example: "Open the terminal and clone the project with git.",
    review_status: "New",
    source_apa: "GitHub, Inc. (2026). About the terminal. In GitHub Docs. https://docs.github.com/",
  },
  {
    id: "lab-repository",
    word: "repository",
    module: "Lab & Tools",
    pos: "noun",
    phonetic: "/rɪˈpɒzɪtəri/",
    en_definition:
      "A storage location for software projects, often tracking version history.",
    zh_meaning: "代码仓库；存放软件项目并常带版本历史的位置。",
    example: "Push your changes to the remote repository before the lab deadline.",
    review_status: "New",
    source_apa: "GitHub, Inc. (2026). About repositories. In GitHub Docs. https://docs.github.com/en/repositories",
  },
  {
    id: "lab-endpoint",
    word: "endpoint",
    module: "Lab & Tools",
    pos: "noun",
    phonetic: "/ˈendpɔɪnt/",
    en_definition:
      "A specific URL or address where a service accepts requests and returns data.",
    zh_meaning: "接口端点；服务接收请求并返回数据的特定网址或地址。",
    example: "The mobile app calls an endpoint to fetch weather data.",
    review_status: "New",
    source_apa: "Mozilla Foundation. (2026). Endpoint. In MDN Web Docs. https://developer.mozilla.org/en-US/docs/Glossary/Endpoint",
  },
];

if (typeof MORE_VOCAB !== "undefined") {
  VOCABULARY.push(...MORE_VOCAB);
}

const VOCAB_DB_VERSION = "v2.0";
