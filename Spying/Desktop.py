
# Import modules
try:
    from PIL import ImageGrab
except ImportError:
    print("Please run: pip install pillow")
    raise SystemExit

""" Create desktop screenshot """ 
def Screenshot(filename):
    snapshot = ImageGrab.grab()
    snapshot.save(filename)