/**
 * Static MCQ question bank for career quizzes.
 * Keyed by career name (must match backend creTitle values).
 * Each career has 10 questions with 4 options and a correctAnswer index.
 */
const quizQuestions = {
  'Full Stack Developer': [
    {
      question: 'What does REST stand for in the context of web APIs?',
      options: [
        'Representational State Transfer',
        'Remote Execution Service Technology',
        'Reliable Stateless Transport',
        'Resource Extraction and Storage Technique',
      ],
      correctAnswer: 0,
    },
    {
      question: 'Which HTTP method is typically used to update an existing resource?',
      options: ['GET', 'POST', 'PUT', 'DELETE'],
      correctAnswer: 2,
    },
    {
      question: 'In the MERN stack, what does the "M" stand for?',
      options: ['MySQL', 'MongoDB', 'MariaDB', 'Memcached'],
      correctAnswer: 1,
    },
    {
      question: 'What is the purpose of middleware in Express.js?',
      options: [
        'To compile JavaScript to machine code',
        'To process requests between receiving and sending a response',
        'To manage database connections only',
        'To render HTML templates on the client side',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which CSS property is used to create a flexible box layout?',
      options: ['display: grid', 'display: flex', 'display: block', 'display: inline'],
      correctAnswer: 1,
    },
    {
      question: 'What does CORS stand for in web development?',
      options: [
        'Cross-Origin Resource Sharing',
        'Client-Originated Request Service',
        'Cache-Optimized Resource System',
        'Centralized Origin Routing Service',
      ],
      correctAnswer: 0,
    },
    {
      question: 'Which React hook is used to manage component state?',
      options: ['useEffect', 'useState', 'useRef', 'useMemo'],
      correctAnswer: 1,
    },
    {
      question: 'What is the primary purpose of a CDN?',
      options: [
        'To write server-side code',
        'To deliver content from geographically closer servers',
        'To encrypt database records',
        'To compile frontend assets',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which status code indicates a resource was successfully created?',
      options: ['200', '201', '204', '301'],
      correctAnswer: 1,
    },
    {
      question: 'What is the Virtual DOM in React?',
      options: [
        'A browser extension for debugging',
        'A lightweight in-memory representation of the real DOM',
        'A server-side rendering engine',
        'A CSS framework for React components',
      ],
      correctAnswer: 1,
    },
  ],

  'Data Scientist': [
    {
      question: 'Which Python library is primarily used for data manipulation and analysis?',
      options: ['NumPy', 'Pandas', 'Matplotlib', 'Scikit-learn'],
      correctAnswer: 1,
    },
    {
      question: 'What does SQL stand for?',
      options: [
        'Structured Query Language',
        'Simple Question Logic',
        'Standard Query Library',
        'Sequential Query Loader',
      ],
      correctAnswer: 0,
    },
    {
      question: 'Which metric is best suited for evaluating classification models with imbalanced classes?',
      options: ['Accuracy', 'F1 Score', 'Mean Squared Error', 'R-squared'],
      correctAnswer: 1,
    },
    {
      question: 'What is the purpose of feature scaling in machine learning?',
      options: [
        'To increase the number of features',
        'To normalize feature ranges so no single feature dominates',
        'To remove outliers from the dataset',
        'To convert categorical data to numerical',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which visualization is best for showing the distribution of a single numerical variable?',
      options: ['Scatter plot', 'Histogram', 'Pie chart', 'Line chart'],
      correctAnswer: 1,
    },
    {
      question: 'What is overfitting in a machine learning model?',
      options: [
        'The model performs well on both training and test data',
        'The model memorizes training data and performs poorly on new data',
        'The model is too simple to capture patterns',
        'The model has too few parameters',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which technique is used to handle missing values in a dataset?',
      options: ['Normalization', 'Imputation', 'Regularization', 'Augmentation'],
      correctAnswer: 1,
    },
    {
      question: 'What does EDA stand for in data science?',
      options: [
        'Exploratory Data Analysis',
        'Experimental Data Architecture',
        'Enhanced Data Aggregation',
        'External Data Assessment',
      ],
      correctAnswer: 0,
    },
    {
      question: 'Which algorithm is commonly used for dimensionality reduction?',
      options: ['Random Forest', 'PCA', 'K-Means', 'Logistic Regression'],
      correctAnswer: 1,
    },
    {
      question: 'What is a p-value in statistical hypothesis testing?',
      options: [
        'The probability of the model being correct',
        'The probability of observing results as extreme as the data assuming the null hypothesis is true',
        'The percentage of variance explained',
        'The prediction accuracy of the model',
      ],
      correctAnswer: 1,
    },
  ],

  'Machine Learning Engineer': [
    {
      question: 'Which of the following is a supervised learning algorithm?',
      options: ['K-Means Clustering', 'PCA', 'Linear Regression', 'DBSCAN'],
      correctAnswer: 2,
    },
    {
      question: 'What is the purpose of a loss function in neural networks?',
      options: [
        'To initialize weights randomly',
        'To measure the difference between predicted and actual values',
        'To split data into train and test sets',
        'To visualize model architecture',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which optimization algorithm is most commonly used in deep learning?',
      options: ['Gradient Descent', 'Adam', 'Simulated Annealing', 'Genetic Algorithm'],
      correctAnswer: 1,
    },
    {
      question: 'What does CNN stand for in deep learning?',
      options: [
        'Convolutional Neural Network',
        'Connected Node Network',
        'Computed Numeric Network',
        'Centralized Neural Nexus',
      ],
      correctAnswer: 0,
    },
    {
      question: 'What is the purpose of dropout in neural networks?',
      options: [
        'To speed up training',
        'To prevent overfitting by randomly disabling neurons',
        'To increase the learning rate',
        'To add more layers to the network',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which framework is developed by Google for machine learning?',
      options: ['PyTorch', 'TensorFlow', 'Scikit-learn', 'Caffe'],
      correctAnswer: 1,
    },
    {
      question: 'What is transfer learning?',
      options: [
        'Training a model from scratch on new data',
        'Using a pre-trained model as a starting point for a new task',
        'Transferring data between databases',
        'Moving a model from GPU to CPU',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What is the vanishing gradient problem?',
      options: [
        'When gradients become too large during training',
        'When gradients become extremely small, preventing weight updates in earlier layers',
        'When the model runs out of memory',
        'When the learning rate is set too high',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which technique is used to evaluate model performance using all data for both training and testing?',
      options: ['Train-test split', 'Cross-validation', 'Bootstrapping', 'A/B testing'],
      correctAnswer: 1,
    },
    {
      question: 'What is an epoch in the context of training a neural network?',
      options: [
        'A single forward pass through one data sample',
        'One complete pass through the entire training dataset',
        'The time taken to train the model',
        'The number of layers in the network',
      ],
      correctAnswer: 1,
    },
  ],

  'Backend Developer': [
    {
      question: 'What is the primary purpose of an ORM?',
      options: [
        'To optimize frontend rendering',
        'To map database tables to objects in programming languages',
        'To manage network requests',
        'To handle user authentication only',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which database type is best suited for storing hierarchical or graph-like data?',
      options: ['Relational (SQL)', 'Graph database', 'Key-value store', 'Column-family store'],
      correctAnswer: 1,
    },
    {
      question: 'What does ACID stand for in database transactions?',
      options: [
        'Atomicity, Consistency, Isolation, Durability',
        'Authentication, Caching, Integration, Deployment',
        'Asynchronous, Concurrent, Idempotent, Distributed',
        'Access, Control, Identity, Data',
      ],
      correctAnswer: 0,
    },
    {
      question: 'Which caching strategy returns data from cache first, then updates from the database?',
      options: ['Write-through', 'Write-behind', 'Cache-aside (Lazy loading)', 'Read-through'],
      correctAnswer: 2,
    },
    {
      question: 'What is the purpose of database indexing?',
      options: [
        'To encrypt sensitive data',
        'To speed up data retrieval operations',
        'To backup database records',
        'To normalize database tables',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which protocol is commonly used for real-time bidirectional communication?',
      options: ['HTTP', 'FTP', 'WebSocket', 'SMTP'],
      correctAnswer: 2,
    },
    {
      question: 'What is a message queue used for in backend systems?',
      options: [
        'To render user interfaces',
        'To decouple services and handle asynchronous processing',
        'To store user sessions',
        'To compile server-side code',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What does JWT stand for?',
      options: [
        'Java Web Token',
        'JSON Web Token',
        'JavaScript Worker Thread',
        'Just-in-time Web Transfer',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which HTTP header is used to prevent CSRF attacks?',
      options: ['Content-Type', 'Authorization', 'X-CSRF-Token', 'Accept'],
      correctAnswer: 2,
    },
    {
      question: 'What is rate limiting in API design?',
      options: [
        'Limiting the database query speed',
        'Restricting the number of API requests a client can make in a time period',
        'Reducing the response payload size',
        'Limiting the number of database connections',
      ],
      correctAnswer: 1,
    },
  ],

  'Frontend Developer': [
    {
      question: 'What is the CSS Box Model composed of?',
      options: [
        'Header, Body, Footer, Sidebar',
        'Content, Padding, Border, Margin',
        'Flex, Grid, Block, Inline',
        'Width, Height, Color, Font',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which JavaScript method is used to select an element by its ID?',
      options: [
        'document.querySelector()',
        'document.getElementById()',
        'document.getElementsByClassName()',
        'document.querySelectorAll()',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What is the purpose of the "key" prop in React lists?',
      options: [
        'To style list items uniquely',
        'To help React identify which items have changed, been added, or removed',
        'To encrypt list data',
        'To set the display order of items',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which CSS unit is relative to the font-size of the root element?',
      options: ['em', 'rem', 'px', 'vh'],
      correctAnswer: 1,
    },
    {
      question: 'What does the "useEffect" hook do in React?',
      options: [
        'Manages component state',
        'Performs side effects like data fetching and DOM manipulation',
        'Memoizes expensive computations',
        'Creates refs to DOM elements',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What is event delegation in JavaScript?',
      options: [
        'Assigning events to every child element individually',
        'Attaching a single event listener to a parent element to handle events on children',
        'Preventing events from bubbling up the DOM',
        'Creating custom events',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which tool is commonly used for bundling JavaScript modules?',
      options: ['ESLint', 'Webpack', 'Prettier', 'Jest'],
      correctAnswer: 1,
    },
    {
      question: 'What is the difference between "==" and "===" in JavaScript?',
      options: [
        'There is no difference',
        '"==" checks value only, "===" checks value and type',
        '"==" is for strings, "===" is for numbers',
        '"==" is deprecated, "===" is the modern version',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What is a closure in JavaScript?',
      options: [
        'A way to close browser windows',
        'A function that has access to variables from its outer scope even after the outer function has returned',
        'A method to end JavaScript execution',
        'A way to lock object properties',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which HTML5 element is used for navigation links?',
      options: ['<div>', '<nav>', '<section>', '<header>'],
      correctAnswer: 1,
    },
  ],

  'DevOps Engineer': [
    {
      question: 'What does CI/CD stand for?',
      options: [
        'Code Integration / Code Deployment',
        'Continuous Integration / Continuous Delivery',
        'Centralized Infrastructure / Centralized Delivery',
        'Container Integration / Container Deployment',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which tool is used for container orchestration at scale?',
      options: ['Docker', 'Kubernetes', 'Ansible', 'Terraform'],
      correctAnswer: 1,
    },
    {
      question: 'What is Infrastructure as Code (IaC)?',
      options: [
        'Writing application code for infrastructure companies',
        'Managing and provisioning infrastructure through machine-readable configuration files',
        'Coding directly on server hardware',
        'A programming language for network devices',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which command is used to build a Docker image from a Dockerfile?',
      options: ['docker run', 'docker build', 'docker pull', 'docker create'],
      correctAnswer: 1,
    },
    {
      question: 'What is the purpose of a load balancer?',
      options: [
        'To store application logs',
        'To distribute incoming traffic across multiple servers',
        'To encrypt network traffic',
        'To manage database replicas',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which tool is commonly used for configuration management?',
      options: ['Git', 'Ansible', 'Docker', 'Prometheus'],
      correctAnswer: 1,
    },
    {
      question: 'What does a reverse proxy do?',
      options: [
        'Connects directly to the internet bypassing the server',
        'Sits in front of servers and forwards client requests to appropriate backend servers',
        'Reverses the direction of network traffic',
        'Encrypts outgoing traffic only',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What is the purpose of monitoring tools like Prometheus?',
      options: [
        'To write application code',
        'To collect, store, and query metrics from systems and applications',
        'To deploy containers',
        'To manage Git repositories',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What is a Kubernetes Pod?',
      options: [
        'A virtual machine in the cloud',
        'The smallest deployable unit that can contain one or more containers',
        'A networking switch',
        'A storage volume',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which practice involves automatically running tests on every code commit?',
      options: [
        'Manual testing',
        'Continuous Integration',
        'Code review',
        'Canary deployment',
      ],
      correctAnswer: 1,
    },
  ],

  'Cybersecurity Analyst': [
    {
      question: 'What is the CIA triad in cybersecurity?',
      options: [
        'Central Intelligence Agency triad',
        'Confidentiality, Integrity, Availability',
        'Cryptography, Identity, Authentication',
        'Control, Isolation, Access',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What type of attack involves tricking users into revealing sensitive information?',
      options: ['DDoS attack', 'Phishing', 'SQL injection', 'Buffer overflow'],
      correctAnswer: 1,
    },
    {
      question: 'What is the purpose of a firewall?',
      options: [
        'To encrypt hard drives',
        'To monitor and filter incoming and outgoing network traffic',
        'To scan for viruses',
        'To manage user passwords',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What does OWASP stand for?',
      options: [
        'Open Web Application Security Project',
        'Online Web Authentication Security Protocol',
        'Organizational Web Access Security Policy',
        'Open Wireless Application Security Platform',
      ],
      correctAnswer: 0,
    },
    {
      question: 'What is a zero-day vulnerability?',
      options: [
        'A vulnerability that has been patched',
        'A previously unknown vulnerability with no available fix',
        'A vulnerability discovered on the first day of deployment',
        'A vulnerability that only affects new software',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which encryption type uses the same key for both encryption and decryption?',
      options: ['Asymmetric encryption', 'Symmetric encryption', 'Hashing', 'Digital signatures'],
      correctAnswer: 1,
    },
    {
      question: 'What is penetration testing?',
      options: [
        'Testing network bandwidth speed',
        'Authorized simulated attacks to evaluate system security',
        'Testing software for bugs',
        'Monitoring employee internet usage',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What does MFA stand for?',
      options: [
        'Multiple Firewall Architecture',
        'Multi-Factor Authentication',
        'Managed File Access',
        'Master Fraud Alert',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which tool is commonly used for network packet analysis?',
      options: ['Nmap', 'Wireshark', 'Metasploit', 'Burp Suite'],
      correctAnswer: 1,
    },
    {
      question: 'What is the principle of least privilege?',
      options: [
        'Giving all users administrative access',
        'Granting users only the minimum access rights needed to perform their tasks',
        'Restricting internet access to all employees',
        'Encrypting all files by default',
      ],
      correctAnswer: 1,
    },
  ],

  'Cloud Engineer': [
    {
      question: 'What does IaaS stand for in cloud computing?',
      options: [
        'Internet as a Service',
        'Infrastructure as a Service',
        'Integration as a Service',
        'Identity as a Service',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which AWS service is used for object storage?',
      options: ['EC2', 'S3', 'RDS', 'Lambda'],
      correctAnswer: 1,
    },
    {
      question: 'What is serverless computing?',
      options: [
        'Computing without any servers',
        'A model where the cloud provider manages server infrastructure and auto-scales',
        'Running code only on local machines',
        'A server with no operating system',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What is the purpose of a Virtual Private Cloud (VPC)?',
      options: [
        'To host websites publicly',
        'To create an isolated network within the cloud',
        'To store encrypted files',
        'To manage DNS records',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which cloud deployment model keeps data and applications within an organization?',
      options: ['Public cloud', 'Private cloud', 'Hybrid cloud', 'Community cloud'],
      correctAnswer: 1,
    },
    {
      question: 'What is auto-scaling in cloud environments?',
      options: [
        'Manually adding more servers',
        'Automatically adjusting compute resources based on demand',
        'Scaling down to zero servers',
        'Increasing storage capacity only',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which service model provides a platform for developers to build applications without managing infrastructure?',
      options: ['IaaS', 'PaaS', 'SaaS', 'FaaS'],
      correctAnswer: 1,
    },
    {
      question: 'What is a CDN commonly used for in cloud architecture?',
      options: [
        'Database replication',
        'Caching and delivering content from edge locations closer to users',
        'Managing IAM policies',
        'Running batch processing jobs',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What does IAM stand for in cloud services?',
      options: [
        'Internet Access Management',
        'Identity and Access Management',
        'Infrastructure and Application Monitoring',
        'Integrated API Management',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which strategy involves running applications in multiple geographic locations for high availability?',
      options: [
        'Single-region deployment',
        'Multi-region deployment',
        'On-premises hosting',
        'Edge computing',
      ],
      correctAnswer: 1,
    },
  ],

  'Mobile App Developer': [
    {
      question: 'Which framework allows building mobile apps using JavaScript for both iOS and Android?',
      options: ['Swift', 'React Native', 'Kotlin', 'Flutter'],
      correctAnswer: 1,
    },
    {
      question: 'What is the purpose of a mobile app lifecycle?',
      options: [
        'To define the app store listing',
        'To manage the different states an app goes through from launch to termination',
        'To track app downloads',
        'To schedule push notifications',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which programming language is primarily used for native iOS development?',
      options: ['Java', 'Kotlin', 'Swift', 'Dart'],
      correctAnswer: 2,
    },
    {
      question: 'What is the purpose of AsyncStorage in React Native?',
      options: [
        'To make API calls',
        'To persist simple key-value data locally on the device',
        'To manage navigation state',
        'To render asynchronous components',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What is a responsive design approach in mobile development?',
      options: [
        'Designing only for the latest phones',
        'Adapting the UI layout to fit different screen sizes and orientations',
        'Making apps respond faster',
        'Using only native components',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which tool is used for debugging React Native applications?',
      options: ['Xcode only', 'Flipper', 'Visual Studio', 'Eclipse'],
      correctAnswer: 1,
    },
    {
      question: 'What is the difference between a native app and a hybrid app?',
      options: [
        'There is no difference',
        'Native apps are built for a specific platform, hybrid apps use web technologies wrapped in a native shell',
        'Hybrid apps are faster than native apps',
        'Native apps can only be built with Java',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What is the purpose of push notifications in mobile apps?',
      options: [
        'To update the app in the background',
        'To send timely messages to users even when the app is not active',
        'To push code updates to the device',
        'To transfer files between devices',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which state management solution is commonly used in Flutter?',
      options: ['Redux', 'Provider', 'MobX', 'Vuex'],
      correctAnswer: 1,
    },
    {
      question: 'What does APK stand for in Android development?',
      options: [
        'Android Programming Kit',
        'Android Package Kit',
        'Application Process Kernel',
        'Android Platform Kernel',
      ],
      correctAnswer: 1,
    },
  ],

  'AI Engineer': [
    {
      question: 'What is the Transformer architecture primarily known for?',
      options: [
        'Image classification',
        'Self-attention mechanism for processing sequential data',
        'Reinforcement learning',
        'Database optimization',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What does GPT stand for?',
      options: [
        'General Purpose Technology',
        'Generative Pre-trained Transformer',
        'Graph Processing Tool',
        'Gradient Propagation Technique',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What is the purpose of attention mechanism in neural networks?',
      options: [
        'To reduce model size',
        'To allow the model to focus on relevant parts of the input when producing output',
        'To speed up training time',
        'To normalize input data',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which technique is used to fine-tune large language models efficiently?',
      options: ['Data augmentation', 'LoRA (Low-Rank Adaptation)', 'Batch normalization', 'Pruning'],
      correctAnswer: 1,
    },
    {
      question: 'What is a GAN (Generative Adversarial Network)?',
      options: [
        'A network for graph analysis',
        'Two neural networks competing: a generator creates data and a discriminator evaluates it',
        'A type of recurrent neural network',
        'A database management system',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What is prompt engineering?',
      options: [
        'Building hardware for AI systems',
        'Designing and optimizing input prompts to get desired outputs from AI models',
        'Engineering the training pipeline',
        'Creating new programming languages for AI',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What is RAG (Retrieval-Augmented Generation)?',
      options: [
        'A type of neural network architecture',
        'Combining retrieval of external knowledge with language generation',
        'A data preprocessing technique',
        'A random gradient algorithm',
      ],
      correctAnswer: 1,
    },
    {
      question: 'What is the purpose of tokenization in NLP?',
      options: [
        'To encrypt text data',
        'To break text into smaller units (tokens) for model processing',
        'To translate text between languages',
        'To compress text files',
      ],
      correctAnswer: 1,
    },
    {
      question: 'Which evaluation metric measures the quality of generated text by comparing it to reference text?',
      options: ['Accuracy', 'BLEU score', 'F1 Score', 'AUC-ROC'],
      correctAnswer: 1,
    },
    {
      question: 'What is model inference?',
      options: [
        'Training a model on new data',
        'Using a trained model to make predictions on new inputs',
        'Evaluating model architecture',
        'Debugging model errors',
      ],
      correctAnswer: 1,
    },
  ],
};

export default quizQuestions;
