def evaluate_notebook(notebook):
    result = {
        "score": 0,
        "feedback": "",
        "summary": "",
        "metrics": {}
    }

    code_cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
    markdown_cells = [cell for cell in notebook.cells if cell.cell_type == "markdown"]

    # Simple evaluation logic (you can expand this)
    code_lines = sum(len(cell.source.strip().split("\n")) for cell in code_cells)
    has_comments = any("#" in cell.source for cell in code_cells)
    uses_pandas = any("import pandas" in cell.source for cell in code_cells)
    uses_numpy = any("import numpy" in cell.source for cell in code_cells)

    score = 0
    score += 20 if code_lines > 10 else 10
    score += 20 if has_comments else 0
    score += 20 if len(markdown_cells) > 0 else 0
    score += 20 if uses_pandas or uses_numpy else 0

    result["score"] = score
    result["summary"] = "Basic notebook structure analysis"
    result["metrics"] = {
        "total_code_cells": len(code_cells),
        "total_markdown_cells": len(markdown_cells),
        "uses_comments": has_comments,
        "uses_pandas_or_numpy": uses_pandas or uses_numpy
    }

    if score >= 70:
        result["feedback"] = "Great job! Your notebook has good structure and documentation."
    elif score >= 40:
        result["feedback"] = "Decent work. Try adding more comments or markdown explanations."
    else:
        result["feedback"] = "Needs improvement. Add markdown, comments, and use standard libraries."

    return result
