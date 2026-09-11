from model import model_lead
import control

def add_lead():
    name=input("Nome:")
    email=input("E-mail:")
    stage=input("Vendas:")

    model_lead((name, email, stage))

    print(model_lead(name,email, stage))
    control.create_lead(model_lead(name, email, stage))

def list_leads():
    leads = control.read_leads()
    print(leads)
def main():
    while True:
        print("Mini CRM de Leads")
        print("[1] adicionar leads")
        print("[2] lista leads")
        print("[0] Sair do programa")

        opt = input("escolha uma opção:")
        if opt =="1":
            print()
        elif opt=="2":
            print()
        elif opt=="0":
            print("Até mais")
            break
        else:
            print("Opção inválida")

if __name__=="__main__":
    main()