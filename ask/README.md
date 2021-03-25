## 環境
```
npm install -g ask-cli
```


&nbsp;


## デプロイ方法
本AlexaスキルではバックエンドにAWS Lambdaを使用せず、独自のバックエンドを使用します。
そのためAlexaスキルをデプロイする際には _スキル名/skill-package/skill.json_ ファイルを修正する必要があります。
ファイル中のmanifest.apis.custom.endpoint.uriの値を使用するバックエンドのURLに変更して下さい。

```
cat scenario1/skill-package/skill.json
{
  "manifest": {
    "apis": {
      "custom": {
        "endpoint": {
          "sslCertificateType": "Wildcard",
          "uri": "https://4986f8d808d1.ap.ngrok.io/" #使用するバックエンドのURLに変更する必要有
        },
        "interfaces": []
      }
    },
    "manifestVersion": "1.0",
    "publishingInformation": {
      "category": "KNOWLEDGE_AND_TRIVIA",
      "distributionCountries": [],
      "isAvailableWorldwide": true,
      "locales": {
        "ja-JP": {
          "description": "Sample Full Description",
          "examplePhrases": [
            "アレクサ、ハローワールドを開いて",
            "こんにちは",
            "ヘルプ"
          ],
          "keywords": [],
          "name": "シナリオI",
          "summary": "Sample Short Description"
        }
      },
      "testingInstructions": "Sample Testing Instructions."
    }
  }
}
```

下記の手順に従うことでAlexaスキルをデプロイすることができます。

```
$ cd scenario1
$ ask init
This utility will walk you through creating an ask-resources.json file to help deploy
your skill. This only covers the most common attributes and will suggest sensible
defaults using AWS Lambda as your endpoint.

This command is supposed to be running at the root of your ask-cli project, with the
Alexa skill package and AWS Lambda code downloaded already.
- Use "ask smapi export-package" to download the skill package.
- Move your Lambda code into this folder depending on how you manage the code. It can
be downloaded from AWS console, or git-cloned if you use git to control version.

This will utilize your 'default' ASK profile. Run with "--profile" to specify a
different profile.

Press ^C at any time to quit.

? Skill Id (leave empty to create one): **空欄**
? Skill package path:  ./skill-package
? Lambda code path for default region (leave empty to not deploy Lambda): **空欄**

Writing to /home/taichi/workspace/ams/ask/scenario1/ask-resources.json:
{
  "askcliResourcesVersion": "xxxx-xx-xx",
  "profiles": {
    "default": {
      "skillMetadata": {
        "src": "./skill-package"
      }
    }
  }
}

Writing to /home/taichi/workspace/ams/ask/scenario1/.ask/ask-states.json:
{
  "askcliStatesVersion": "xxxx-xx-xx",
  "profiles": {
    "default": {
      "skillId": ""
    }
  }
}

? Does this look correct?  Yes

Success! Run "ask deploy" to deploy your skill.

$ ask deploy
Deploy configuration loaded from ask-resources.json
Deploy project for profile [default]

==================== Deploy Skill Metadata ====================
Skill package deployed successfully.
Skill ID: xxxxx.ask.skill.xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

==================== Enable Skill ====================
Skill is enabled successfully.
```
