from buildozer.scripts.client import main
import sys

if __name__ == "__main__":
    # تنظیم آرگومان‌های خط فرمان
    sys.argv = ['buildozer', 'android', 'debug']
    
    # اجرای Buildozer
    print("🚀 Starting Buildozer...")
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}")
        input("Press Enter to exit...")
