#!/usr/bin/env fontforge
import fontforge
import sys

def create_font_subset(input_font, output_font, chars):
    """
    Create a subset of a font containing only specified characters.
    
    Args:
        input_font (str): Path to the input font file
        output_font (str): Path where the new font will be saved
        chars (str): String containing all characters to keep in the subset
    """
    # Open the font
    font = fontforge.open(input_font)
    
    # Create a list of all codepoints in the font
    all_codepoints = []
    for glyph in font.glyphs():
        if glyph.unicode != -1:  # -1 means no unicode value assigned
            all_codepoints.append(glyph.unicode)
    
    # Convert input characters to codepoints
    keep_codepoints = set(ord(c) for c in chars)
    
    # Find codepoints to remove (those in font but not in our keep list)
    remove_codepoints = set(all_codepoints) - keep_codepoints
    
    # Remove unwanted glyphs
    for codepoint in remove_codepoints:
        if font.selection.select(("more", "unicode"), codepoint):
            font.clear()
    
    # Generate new font
    font.generate(output_font)
    font.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: fontforge -script subset_font.py input_font.ttf output_font.ttf")
        sys.exit(1)
    
    input_font = sys.argv[1]
    output_font = sys.argv[2]
    chars = ["A", "閒"]
    
    create_font_subset(input_font, output_font, chars)