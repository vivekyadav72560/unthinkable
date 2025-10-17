import google.generativeai as genai
import os

# Configure the API key
# Make sure to set your GOOGLE_API_KEY environment variable
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

def generate_explanation(user_history, recommended_product):
    """Generates a personalized explanation for a recommendation."""
    
    # Create a summary of user's past behavior
    history_summary = []
    if not user_history:
        history_summary.append("This user is new.")
    else:
        for product in user_history:
            history_summary.append(f"- '{product.name}' (Category: {product.category})")
    
    history_text = "\n".join(history_summary)

    # Construct the prompt for the LLM
    prompt = f"""
    You are an expert E-commerce recommender system. Your task is to explain why a product is a good recommendation for a user based on their past interactions.

    **User's Past Interactions:**
    {history_text}

    **Recommended Product:**
    - Name: {recommended_product.name}
    - Category: {recommended_product.category}
    - Description: {recommended_product.description}

    **Your Task:**
    Generate a short, friendly, and persuasive explanation (2-3 sentences) for the user about why they might like this recommended product. Connect it to their past behavior if possible. Address the user directly ("You might like...").
    
    **Explanation:**
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error generating explanation: {e}")
        return "You might like this product because it's popular among users with similar tastes!"