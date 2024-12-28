import json
from emo_platform import Client, Tokens, Head, Color


def get_emo_cred():
    with open("credentials/emo/emo.json", "r") as f:
        return json.load(f)


cred = get_emo_cred()
client = Client(
    tokens=Tokens(
        access_token=cred["access_token"], refresh_token=cred["refresh_token"]
    )
)

motions = client.get_motions_list()
print("Available motions:", motions)


room_id_list = client.get_rooms_id()
import random

room_client = client.create_room_client(room_id_list[0])
try:
    motions = [
        {"name": "Bonbori_short", "uuid": "fa0beb73-ce8f-4786-9c0b-05ea5da9f125"},
        {"name": "ALRIGHT_H_1", "uuid": "790de5c1-0a7e-47c1-861d-04df16cda7de"},
        {"name": "ALRIGHT_W_3", "uuid": "caf9afb6-86ee-44a7-8eba-209d707af46f"},
        {"name": "ALRIGHT_N_0", "uuid": "117867c0-3668-407b-bf8d-ad7858c6bff2"},
        {"name": "ALRIGHT_H_2", "uuid": "a58e8a21-4ecd-4ff8-9311-a2f3412ada51"},
        {"name": "ALRIGHT_H_3", "uuid": "6c0eac9f-8130-4247-90d1-b078bc15e431"},
        {"name": "ALRIGHT_A_2", "uuid": "a277d97d-ebf9-47fe-957b-16f268603917"},
        {"name": "ALRIGHT_W_1", "uuid": "77e4a29e-89b5-4f15-831b-3154e57386e4"},
        {"name": "ALRIGHT_A_3", "uuid": "5b5fbc88-4ae4-421b-b415-39a75ef8c55a"},
        {"name": "ALRIGHT_A_1", "uuid": "855ba700-098b-455a-8fb4-f37e84342569"},
        {"name": "ALRIGHT_W_2", "uuid": "548fd065-4bb2-4b9d-99cd-07f446f1f3df"},
        {"name": "BOCCO_N_0", "uuid": "042807a4-ba11-4478-a386-14a2171eca74"},
        {"name": "BOCCO_H_1", "uuid": "95943120-1ef1-4770-8f87-3c35d3b75fc6"},
        {"name": "BOCCO_H_2", "uuid": "8c393481-8f9b-44da-8407-3a9d77d4327c"},
        {"name": "BOCCO_A_3", "uuid": "166063c5-3013-4b89-8741-3ce17487f881"},
        {"name": "BOCCO_W_2", "uuid": "9ad1212d-0d36-426f-8f3e-e545529cf160"},
        {"name": "BOCCO_A_2", "uuid": "07f7554d-8320-4103-a45f-78a5b42500ad"},
        {"name": "BOCCO_A_1", "uuid": "aeddf4a1-8189-4e13-85ca-3343ae861c39"},
        {"name": "BOCCO_H_3", "uuid": "37ce3705-d22d-42d7-9d43-588d1bc49cc5"},
        {"name": "BOCCO_W_3", "uuid": "b3279fc6-95e2-412f-8423-57a3628faa74"},
        {"name": "BOCCO_W_1", "uuid": "ed1597d7-611c-4c2e-bd55-1bc8a6b9b908"},
        {"name": "EMO_H_1", "uuid": "edab6f55-d05b-4f9b-9dec-c22bebcf1583"},
        {"name": "EMO_A_1", "uuid": "0bff8740-9152-4c48-9191-1aa30a539427"},
        {"name": "EMO_W_3", "uuid": "5b1888ad-d10e-44cf-87fe-c96fe4c17f8c"},
        {"name": "EMO_W_1", "uuid": "11971250-f37c-42f9-aa8e-1e77b79502be"},
        {"name": "EMO_H_2", "uuid": "b656c47f-3567-4797-8232-c21de6e78c9d"},
        {"name": "EMO_A_3", "uuid": "8a3efe66-a363-47e2-b27c-80d57e53d307"},
        {"name": "EMO_W_2", "uuid": "7d300dea-cce5-4673-983c-8abcf5a015c5"},
        {"name": "EMO_H_3", "uuid": "c53d42cd-2daf-454c-b754-b706914681f0"},
        {"name": "EMO_A_2", "uuid": "55d4abfc-3cde-4756-8fbf-e2ae561b8848"},
        {"name": "EMO_N_0", "uuid": "2e7f884a-c3d8-4e24-b797-0e9974854cf4"},
        {"name": "GOOD_W_2", "uuid": "95382142-b922-41a8-aaf0-4f8aa847b47a"},
        {"name": "GOOD_H_1", "uuid": "801e1eac-fd84-4f77-a3ce-20a47eaafd01"},
        {"name": "GOOD_W_3", "uuid": "81db2e5f-d9bd-43f6-9e7d-277111e0a281"},
        {"name": "GOOD_W_1", "uuid": "6d5cf02a-9872-4f8b-8dd5-11f3828f1e57"},
        {"name": "GOOD_A_3", "uuid": "2c465b38-7e71-4320-a3d4-a68c4a6a7408"},
        {"name": "GOOD_H_3", "uuid": "6b4d6b12-7e41-4bc1-a7f5-4747de850678"},
        {"name": "GOOD_N_0", "uuid": "eb6f8204-c551-4fb3-85be-abf3d192956a"},
        {"name": "GOOD_H_2", "uuid": "6c2339e1-b49d-43e3-9969-fea3f887f1d3"},
        {"name": "GOOD_A_1", "uuid": "434a10ab-6927-4af0-94c2-04873ef933a7"},
        {"name": "GOOD_A_2", "uuid": "717d203b-9be8-4d28-9c10-826dcbc63b9d"},
        {"name": "NO_H_1", "uuid": "dae64861-0059-49bd-b345-a1eaf0d998e8"},
        {"name": "NO_N_0", "uuid": "6f390274-2338-44e2-ac9e-7f0e96426114"},
        {"name": "NO_A_2", "uuid": "ec934b7a-66a5-4a15-beaa-ac6475e89048"},
        {"name": "NO_A_3", "uuid": "132e11b2-d23d-4bdb-a2a9-745459ded4b8"},
        {"name": "NO_W_1", "uuid": "2a8f0bc7-9d61-4ffd-a128-b5519d5aaf9e"},
        {"name": "NO_H_3", "uuid": "8c714d8c-eb8e-4480-9ba4-2b4dade4c4d6"},
        {"name": "NO_A_1", "uuid": "fc8061b6-1646-4d82-91bf-25e3dea0145f"},
        {"name": "NO_H_2", "uuid": "d2d7404e-9279-4e57-86b9-10cddde5313c"},
        {"name": "NO_W_3", "uuid": "18600e24-e7ef-4325-b438-5a1ac0fb544d"},
    ]
    random_motion = random.choice(motions)
    print(random_motion["name"])
    room_client.send_motion(random_motion["uuid"])
except Exception as e:
    print(e)
