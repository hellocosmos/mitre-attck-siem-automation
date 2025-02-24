import json

def clean_mitre_data(input_file, output_file):
    # Load the JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # List to store cleaned data
    cleaned_data = []

    # Extract relevant fields
    for item in data.get('objects', []):  # Adjust 'objects' based on the JSON structure
        if item.get('type') == 'attack-pattern':
            cleaned_item = {
                "id": item.get("id"),
                "name": item.get("name"),
                "description": item.get("description"),
                "kill_chain_phases": item.get("kill_chain_phases", []),
                "external_references": [
                    {
                        "source_name": ref.get("source_name"),
                        "url": ref.get("url"),
                        "external_id": ref.get("external_id")
                    }
                    for ref in item.get("external_references", [])
                ]
            }
            cleaned_data.append(cleaned_item)

    # Save cleaned data to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(cleaned_data, f, indent=4)

    print(f"Cleaned data saved to {output_file}")

# Example usage
input_file = './mitre_attack_data.json'  # Replace with your input file path
output_file = './cleaned_mitre_attack_data.json'  # Replace with your desired output file path
clean_mitre_data(input_file, output_file)
