# Serverless AI Data Engineering Pipeline
building serverless pipeline from dynamo db to lambda to sqs to lambda to aws comprehend to s3 

### screenshots
(full terminal session of this example is [here](https://github.com/stevedepp/fp-cloud-formation-clt/blob/main/terminal_session.rtf).)

#

    mkdir folder_name
    cd folder_name
    git clone https://github.com/stevedepp/fp-cloud-formation-clt.git
    cd fp-cloud-formation-clt
    python3 -m venv .venv
    source .venv/bin/activate
    make install

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272288-cfed0980-3758-11eb-889a-b6d14129f4ef.png">

    ./cfcli.py make-infra

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272308-09257980-3759-11eb-975f-7ffc429abae0.png">

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272325-3e31cc00-3759-11eb-865f-071c32bb9088.png">

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272426-0414fa00-375a-11eb-99da-bc3ad2ea2673.png">

`nano ./cos.txt` contains a column of names

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272455-40485a80-375a-11eb-8944-c5f86e70a1ad.png">

    ./cfcli.py add --file ./cos.txt
    ./cfcli.py add -f ./cos.txt

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272463-59e9a200-375a-11eb-98dd-27de2f02e75b.png">

    ./cfcli.py remove --item amazon --item google
    ./cfcli.py remove -i amazon -i google

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272479-95846c00-375a-11eb-8432-7e45081300fe.png">

    ./cfcli.py update --old netflix -new Netflix
    ./cfcli.py update -o netflix -n Netflix

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272494-c8c6fb00-375a-11eb-8366-18b682e7bc6e.png">

    ./cfcli.py remove -i amazon
    ./cfcli.py remove --item amazon

(but amazon isn't there so amazon is ignored)

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272523-fdd34d80-375a-11eb-8adc-91fe5ac44245.png">

    ./cfcli.py update --old amazon -new Amazon
    ./cfcli.py update -o amazon -n Amazon

(since amazon isn't there, amazon is added)

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272549-3410cd00-375b-11eb-876e-ed171e5f4001.png">

    ./cfcli.py teardown

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272564-599dd680-375b-11eb-8894-9e850927f9ea.png">

unfortunately, teardown results in a lot of  
- [x] questions: please answer `y`
- [x] popups: please type `q` and hit the `return` key

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272561-5276c880-375b-11eb-94b5-d71be7630615.png">


<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272566-602c4e00-375b-11eb-91c2-ecf88364ece9.png">

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272569-67535c00-375b-11eb-8417-0a890ead5dd1.png">

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272571-6d493d00-375b-11eb-87ec-b13535978869.png">

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272575-733f1e00-375b-11eb-86a4-73e472d11b44.png">

<img width="682" alt="image" src="https://user-images.githubusercontent.com/38410965/101272577-7c2fef80-375b-11eb-9b39-316cc1184eca.png">
