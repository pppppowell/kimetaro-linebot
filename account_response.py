import random

class Response:

    name = {
        1: "ほいほい",    
        2: "なに",
        3: "ほんほんへ",
        4: "呼んだ？",
        5: "おう",
        6: "なんや",
        7: "はいよ"
    }

    judge = {
        1: "でええんちゃう！？！？",
        2: "でよいのでは",
        3: "にしとこ",
        4: "に決めた",
        5: "がいいと思う！！！！",
        6: "かな～～"
    }

    def nameResponse(self):
        rand=random.randrange(1,len(self.name))
        return self.name[rand]

    def judgeResponse(self):
        rand = random.randrange(1, len(self.judge))
        return self.judge[rand]
    