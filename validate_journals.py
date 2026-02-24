import os
import glob
import yaml

def validate_frontmatter(filepath):
    """Validates the YAML frontmatter of a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [f"Could not read file: {e}"]

    if not content.startswith('---'):
        return ["Missing starting '---' for YAML frontmatter"]

    parts = content.split('---', 2)
    if len(parts) < 3:
        return ["Missing ending '---' for YAML frontmatter"]

    yaml_str = parts[1]
    
    try:
        data = yaml.safe_load(yaml_str)
    except yaml.YAMLError as e:
        return [f"YAML parsing error: {e}"]
        
    if not isinstance(data, dict):
        return ["Frontmatter is not a valid YAML dictionary"]

    # Define the exact required keys expected in the markdown frontmatter
    required_keys = [
        'swemper_filename', 
        'journal_titles', 
        'associated_organisations',
        'year_range_included_in_swemper', 
        'full_years_missing_in_swemper',
        'digitised_by', 
        'libris_id', 
        'alvin_id', 
        'sources'
    ]
    
    errors = []
    for key in required_keys:
        if key not in data:
            errors.append(f"Missing key '{key}'")
            
    # Optional: check if some fields are valid lists if they exist
    list_keys = ['journal_titles', 'associated_organisations', 'digitised_by', 'libris_id', 'sources']
    for key in list_keys:
        if key in data and data[key] is not None:
            if not isinstance(data[key], list):
                errors.append(f"Key '{key}' should be a list/sequence")

    return errors

def main():
    directory = 'journal_descriptions'
    
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' not found.")
        return

    md_files = glob.glob(os.path.join(directory, '*.md'))
    if not md_files:
        print(f"No .md files found in '{directory}'.")
        return

    print(f"Validating {len(md_files)} markdown files in '{directory}'...")
    
    all_errors = {}
    
    for filepath in md_files:
        errors = validate_frontmatter(filepath)
        if errors:
            all_errors[filepath] = errors

    if all_errors:
        print("\n❌ Validation Failed. Found errors in the following files:")
        for filepath, errors in all_errors.items():
            print(f"\n{os.path.basename(filepath)}:")
            for error in errors:
                print(f"  - {error}")
        import sys
        sys.exit(1)
    else:
        print(f"\n✅ All {len(md_files)} files validated successfully!")

if __name__ == '__main__':
    main()
