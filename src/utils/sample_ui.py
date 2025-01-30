import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("LLM Response Evaluator")

# Text input
user_input = st.text_area("Enter text to evaluate:", height=150)

# Evaluate button
if st.button("Evaluate"):
    if user_input:
        # Call the API endpoint
        response = requests.post(
            "http://localhost:8000/evaluate_response",
            data=user_input,
            headers={'Content-Type': 'text/plain'}
        )
        
        if response.status_code == 200:
            result = response.json()['result']
            
            # Create DataFrame for display
            df = pd.DataFrame({
                'Sentence': [user_input],
                'Gibberish Class': [result['gibberish']['class']],
                'Gibberish Score': [round(result['gibberish']['score'], 3)],
                'Hallucination Score': [round(result['hallucination'], 3)]
            })
            
            # Display table
            st.subheader("Evaluation Results")
            st.dataframe(df, hide_index=True)
            
            # Create bar chart using matplotlib
            fig, ax = plt.subplots()
            scores = [result['gibberish']['score'], result['hallucination']]
            labels = ['Gibberish Score', 'Hallucination Score']
            bars = ax.bar(labels, scores)
            
            # Customize the plot
            ax.set_title('Evaluation Scores')
            ax.set_ylabel('Score')
            ax.set_ylim(0, 1)
            
            # Add value labels on top of bars
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.3f}',
                       ha='center', va='bottom')
            
            st.pyplot(fig)
            
        else:
            st.error("Error calling the API")
    else:
        st.warning("Please enter some text to evaluate")

