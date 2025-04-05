# 📸 azure-image-analyzer

A simple serverless app that analyzes images using **Azure Functions** and **Python**.  
When you upload an image to **Azure Blob Storage**, it triggers a function that uses **Azure's Computer Vision API** to detect objects, tags, and text.

## 🔧 Features

- Serverless architecture with Azure Functions
- Image analysis using Azure's Computer Vision API
- Event-driven: Triggers when an image is uploaded to Blob Storage
- Built with **Python**

## 🚀 Getting Started

### Prerequisites

- [Azure account](https://azure.microsoft.com/free)
- [Python 3.x](https://www.python.org/)
- [Azure Functions Core Tools](https://docs.microsoft.com/azure/azure-functions/functions-run-local) (for local development)

### Setup

1. **Clone this repo:**

   ```bash
   git clone https://github.com/mejia-b/azure-image-analyzer.git
   cd azure-image-analyzer

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

3. **Create an Azure Function:**

   - Follow the [Azure Functions documentation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal?pivots=programming-language-csharp) to create a function app.
   - Configure Blob Storage trigger in the function.

4. **Configure Azure Cognitive Services (Computer Vision)**
   - Set up [Azure Computer Vision API](https://azure.microsoft.com/en-us/products/ai-services/ai-vision/) and get the API key.
   - Add the API key to your local.settings.json or environment variables.
  
5. **Run the function locally:**

   ```bash
   func start

6. **Deploy to Azure:**
   Once you have tested your function locally, deploy it to Azure:
   - Follow the [Azure deployment guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference?tabs=blob&pivots=programming-language-csharp#deployment) to deploy your function to Azure.
     
### 💻 Contributing
Feel free to fork this project and submit issues or pull requests. 
If you have suggestions or improvements, please open an issue!

### 📄License
This project is licensed under the MIT License.

   

