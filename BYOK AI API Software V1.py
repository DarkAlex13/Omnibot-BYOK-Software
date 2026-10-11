import sys
import time

print("Welcome to your OFFLINE testing client.")
print("Type 'exit' or 'quit' at any time to stop.")

# Memory list (even though the fake AI doesn't really use it, it's good for testing)
chat_context = []

while True:
    user_text = input("\nYou: ").strip()
    
    if user_text.lower() in ['exit', 'quit']:
        print("Closing connection. Goodbye!")
        break
        
    if not user_text:
        continue

    # Save user message to memory
    chat_context.append({"role": "user", "content": user_text})
    
    print("AI: ", end="")
    
    # --- THE FAKE AI SIMULATOR ---
    # It creates a fake sentence using your own input
    fake_reply = f"I am a test dummy! I received your message: '{user_text}'. Your chat interface is working perfectly."
    
    # Split the sentence into chunks (words)
    chunks = fake_reply.split()
    
    full_reply = ""
    
    # Print each word one-by-one with a delay to simulate streaming
    for word in chunks:
        print(word + " ", end="")
        sys.stdout.flush() # Force the terminal to show the word instantly
        time.sleep(0.15)   # Wait 0.15 seconds before the next word
        full_reply += word + " "
        
    print() # Add a clean new line when it finishes typing
    
    # Save the full AI response to memory
    chat_context.append({"role": "assistant", "content": full_reply})