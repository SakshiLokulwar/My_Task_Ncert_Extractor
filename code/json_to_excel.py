import json
import pandas as pd
import os

# Define input and output file paths
input_path = os.path.join("json_output", "chapter6.json")
output_path = os.path.join("excel_output", "chapter6_output.xlsx")

# Check if input file exists
if not os.path.exists(input_path):
    print(f"❌ Error: JSON file not found at '{input_path}'")
else:
    # Load the JSON file
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Prepare flat list of rows
    rows = []
    chapter_name = data.get("Chapter", "")

    for topic in data.get("Topics", []):
        topic_title = topic.get("Topic Name", "")

        for subtopic in topic.get("Sub-topics", []):
            subtopic_title = subtopic.get("Sub-topic Name", "")
            for i, paragraph in enumerate(subtopic.get("Content", []), 1):
                rows.append({
                    "Chapter Name": chapter_name,
                    "Topic Title": topic_title,
                    "Sub-topic Title": subtopic_title,
                    "Page No": "",  # Not available in current data
                    "Sequence No": i,
                    "Content Type": "Paragraph",
                    "Internal Name": "",
                    "Actual Content": paragraph
                })

            for activity in subtopic.get("Activities", []):
                rows.append({
                    "Chapter Name": chapter_name,
                    "Topic Title": topic_title,
                    "Sub-topic Title": subtopic_title,
                    "Page No": "",
                    "Sequence No": "",
                    "Content Type": "Activity",
                    "Internal Name": activity.get("Title", ""),
                    "Actual Content": activity.get("Full Description", "")
                })

            for fact in subtopic.get("Boxed Facts or External Info", []):
                rows.append({
                    "Chapter Name": chapter_name,
                    "Topic Title": topic_title,
                    "Sub-topic Title": subtopic_title,
                    "Page No": "",
                    "Sequence No": "",
                    "Content Type": "Boxed Fact",
                    "Internal Name": "",
                    "Actual Content": fact
                })

            for question in subtopic.get("Questions or Exercises", []):
                rows.append({
                    "Chapter Name": chapter_name,
                    "Topic Title": topic_title,
                    "Sub-topic Title": subtopic_title,
                    "Page No": "",
                    "Sequence No": "",
                    "Content Type": "Question or Exercise",
                    "Internal Name": "",
                    "Actual Content": question
                })

    # Convert to DataFrame
    df = pd.DataFrame(rows)

    # Ensure output folder exists
    os.makedirs("excel_output", exist_ok=True)

    # Save to Excel
    df.to_excel(output_path, index=False)
    print(f"✅ Successfully exported to '{output_path}'")

























































































































































































































































































































































'''import json
import pandas as pd
import os

# Define input and output file paths
input_path = os.path.join("json_output", "chapter6.json")
output_path = os.path.join("excel_output", "chapter6_output.xlsx")

# Check if input file exists
if not os.path.exists(input_path):
    print(f"❌ Error: JSON file not found at '{input_path}'")
else:
    # Load the JSON file
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Prepare flat list of rows
    rows = []
    for topic in data["topics"]:
        chapter_number = data.get("chapter_number", "")
        chapter_name = data.get("chapter_name", "")
        topic_number = topic.get("topic_number", "")
        topic_title = topic.get("topic_title", "")

        for content in topic.get("content", []):
            rows.append({
                "Chapter Number": chapter_number,
                "Chapter Name": chapter_name,
                "Topic Number": topic_number,
                "Topic Title": topic_title,
                "Page No": content.get("page_no", ""),
                "Sequence No": content.get("sequence_no", ""),
                "Content Type": content.get("type", ""),
                "Internal Name": content.get("internal_name", ""),
                "Actual Content": content.get("actual_content", "")
            })

    # Convert to DataFrame
    df = pd.DataFrame(rows)

    # Ensure output folder exists
    os.makedirs("excel_output", exist_ok=True)

    # Save to Excel
    df.to_excel(output_path, index=False)
    print(f"✅ Successfully exported to '{output_path}'")'''