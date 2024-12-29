def calculate_grade(score):
    """
    Given a numerical score, returns the letter grade.
    """
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def process_grades(input_file, output_file):
    """
    Reads a list of names and scores from input_file, calculates grades,
    and writes the result to output_file.
    """
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open(output_file, "w", encoding="utf-8") as file:
            for line in lines:
                name, score_str = line.strip().split()
                score = float(score_str)
                grade = calculate_grade(score)
                file.write(f"{name} {grade}\n")
    except Exception as e:
        # Handle exceptions silently; log errors to a file if necessary.
        with open("error.log", "w", encoding="utf-8") as error_file:
            error_file.write(f"Error processing grades: {e}\n")


if __name__ == "__main__":
    # Hardcoded file names for GitHub Actions workflow
    process_grades("notlar.txt", "sonuclar.txt")
