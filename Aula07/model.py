from datetime import date
def model_lead(nome,email,stage):
    return {
        "Nome": nome,
        "email":email,
        "stage":stage,
        "created": date.today().isoformat()

    }