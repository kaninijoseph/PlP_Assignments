import requests
import os
from urllib.parse import urlparse
import mimetypes

def create_ubuntu_image_fetcher():
    """
    Ubuntu-Inspired Image Fetcher
    "I am because we are" - connecting to the global community through shared images
    """
    
    def fetch_image_from_community():
        print("🌍 Ubuntu Image Fetcher: Connecting to the Global Community")
        print("=" * 50)
        
        # Get URL from user with Ubuntu spirit
        url = input("Please share an image URL from our global community: ").strip()
        
        if not url:
            print("🙏 Respect: No URL provided. The community shares through giving.")
            return
        
        try:
            # Respectful connection attempt
            print("🔄 Connecting to the community resource...")
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Check for HTTP errors
            
            # Verify we're getting an image
            content_type = response.headers.get('content-type', '')
            if not content_type.startswith('image/'):
                print("❌ Respect: The shared resource is not an image. Please share visual content.")
                return
            
            # Create community storage
            community_dir = "Fetched_Images"
            os.makedirs(community_dir, exist_ok=True)
            print(f"📁 Community archive '{community_dir}' is ready")
            
            # Determine appropriate filename with respect to the source
            filename = generate_respectful_filename(url, content_type)
            filepath = os.path.join(community_dir, filename)
            
            # Save the  resource
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            print(f"✅ Success: Community image saved as '{filename}'")
            print(f"💾 Location: {filepath}")
            print("🤝 Thank you for sharing with the community!")
            
        except requests.exceptions.RequestException as e:
            handle_errors_with_respect(e)
        except Exception as e:
            print(f"🛑 Unexpected challenge: {e}")
            print("💡 Wisdom: Even in difficulty, we learn and grow together")

    def generate_respectful_filename(url, content_type):
        """Generate a filename that respects the source while being practical"""
        
        # Try to extract filename from URL
        parsed_url = urlparse(url)
        url_path = parsed_url.path
        
        if url_path and '.' in url_path:
            # Use the original filename if available
            original_name = os.path.basename(url_path)
            if original_name and len(original_name) < 100: 
                return original_name
        
        # Generate a community-inspired name
        extension = mimetypes.guess_extension(content_type) or '.jpg'
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"community_image_{timestamp}{extension}"

    def handle_errors_with_respect(error):
        """Handle errors in the spirit of Ubuntu - with understanding and grace"""
        
        error_messages = {
            requests.exceptions.ConnectionError: "🌐 Community Connection Failed: Unable to reach the shared resource",
            requests.exceptions.Timeout: "⏰ Patience: The connection took too long. The community moves at its own pace",
            requests.exceptions.HTTPError: "🔍 Respect: The requested resource is not available (HTTP Error)",
            requests.exceptions.TooManyRedirects: "🔄 Circular Journey: Too many redirects in the community path",
        }
        
        for error_type, message in error_messages.items():
            if isinstance(error, error_type):
                print(message)
                return
        
        print(f"🤔 Learning Opportunity: {error}")

    return fetch_image_from_community

def main():
    """
    Main function embodying Ubuntu principles:
    - Community: Connecting users to shared resources
    - Respect: Graceful error handling
    - Sharing: Organized storage for collective benefit
    - Practicality: Useful tool for everyday needs
    """
    print("=" * 60)
    print("          🌍 UBUNTU IMAGE FETCHER 🌍")
    print("    'I am because we are' - Community Wisdom")
    print("=" * 60)
    print()
    
    fetcher = create_ubuntu_image_fetcher()
    
    while True:
        fetcher()
        print("\n" + "-" * 50)
        
        continue_choice = input("\nWould you like to fetch another community image? (y/n): ").strip().lower()
        if continue_choice not in ['y', 'yes']:
            print("🌅 Thank you for participating in our community!")
            print("May the connections we've made continue to grow 🤝")
            break

if __name__ == "__main__":
    main()