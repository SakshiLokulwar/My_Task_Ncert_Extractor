import json
import os

def generate_knowledge_graph(json_path, output_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    graph_lines = []
    chapter_title = f"Chapter {data['chapter_number']}: {data['chapter_name']}"
    graph_lines.append(f"📘 {chapter_title}")
    
    for topic in data["topics"]:
        topic_header = f"├── 🟢 Topic {topic['topic_number']}: {topic['topic_title']}"
        graph_lines.append(topic_header)
        
        for content in topic.get("content", []):
            content_type = content.get("type", "Unknown")
            internal_name = content.get("internal_name", "")
            short_content = content.get("actual_content", "")[:80].replace('\n', ' ').strip() + "..."
            line = f"│   ├── {content_type} ({internal_name}): {short_content}"
            graph_lines.append(line)

    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(graph_lines))

    print(f"✅ Knowledge graph saved to: {output_path}")


# Call the function to create the knowledge graph from chapter6.json
generate_knowledge_graph(
    "json_output/chapter6.json", 
    "knowledge_graphs/chapter6_knowledge_graph.txt"
)

























































































































































































































































































































































'''import json
import os

def generate_knowledge_graph(json_path, output_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    graph_lines = []
    chapter_title = f"📘 Chapter: {data.get('Chapter', 'Unknown')}"
    graph_lines.append(chapter_title)
    
    for topic in data.get("Topics", []):
        topic_title = topic.get("Topic Name", "Untitled Topic")
        topic_header = f"├── 🟢 Topic: {topic_title}"
        graph_lines.append(topic_header)
        
        for subtopic in topic.get("Sub-topics", []):
            subtopic_title = subtopic.get("Sub-topic Name", "No Sub-topic")
            graph_lines.append(f"│   ├── 🔹 Sub-topic: {subtopic_title}")
            
            for i, para in enumerate(subtopic.get("Content", []), 1):
                short_content = para[:80].replace('\n', ' ').strip() + "..."
                graph_lines.append(f"│   │   ├── 📄 Paragraph {i}: {short_content}")
            
            for activity in subtopic.get("Activities", []):
                title = activity.get("Title", "Activity")
                desc = activity.get("Description", "")
                graph_lines.append(f"│   │   ├── ⚙️ {title}: {desc[:60]}...")

            for fact in subtopic.get("Boxed Facts or External Info", []):
                graph_lines.append(f"│   │   ├── 📌 Fact: {fact[:80]}...")

            for question in subtopic.get("Questions or Exercises", []):
                graph_lines.append(f"│   │   ├── ❓ Question: {question[:80]}...")

    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(graph_lines))

    print(f"✅ Knowledge graph saved to: {output_path}")


# Call the function
generate_knowledge_graph(
    "json_output/chapter13.json", 
    "knowledge_graphs/chapter13_knowledge_graph.txt"
)'''
