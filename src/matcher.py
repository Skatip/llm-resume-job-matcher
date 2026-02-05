
def match_resume(resume, job_desc):
    return {
        "score": 0.82,
        "matched_skills": ["Python", "ML", "NLP"],
        "missing_skills": ["MLOps"],
        "summary": "Strong match with minor gaps"
    }

if __name__ == "__main__":
    print(match_resume("resume.txt", "job.txt"))
