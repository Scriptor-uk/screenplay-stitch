# Script to Screen Formatter

A simple Python utility that helps you create script-to-screen comparison videos by extracting and combining specific script pages into a single image.

[Example Script to Screen Video](https://www.instagram.com/reel/DCRl_SnuhM3/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)

## Usage

1. Run the script
2. Enter your PDF path (or drag & drop the file)
3. Enter page range:
   - Range format: "1-3" (pages 1 through 3)
   - Specific pages: "1,3,5" (pages 1, 3, and 5)

```bash
$ python script_formatter.py
Enter the path to your PDF file: script.pdf
PDF has 120 pages.
Enter page range (e.g., '8-10' or '1,3,5'): 45-47
Successfully created combined_pages.png
```

## Output

- Creates `combined_pages.png` in your current directory
- Pages are combined vertically into a single image
- Ideal for script-to-screen comparison videos

## Tips

- Drag & drop your PDF into terminal for easy path input

## Need Help?

File an issue on GitHub with:

- Your operating system
- The error message
- Details of the issue

## License

MIT License
