# 본 코드는 유튜버 sentdex의 Starcraft 2 AI with Python - Introduction (p.1)영상과 Text-based tutorial의 테스트 코드로
# BurnySc2의 python-sc2 프로젝트 테스트를 위해 사용함 + 주석 한글 번역  

from sc2.bot_ai import BotAI  # 상속받은 부모 클래스
from sc2.data import Difficulty, Race  # 봇 난이도, 사용할 종족 결정을 위한 기능
from sc2.main import run_game  # 게임에서 실제로 에이전트를 실행하는 것을 용이하게 하는 기능
from sc2.player import Bot, Computer  # 에이전트가 봇 또는 "컴퓨터" 플레이어인지 여부를 포장함
from sc2 import maps  # 플레이하기 위한 맵을 로딩하는 방법 Program Files (x86)/StarCraft II/Maps에 맵 파일 넣어야함


class IncrediBot(BotAI): # BotAI로부터 상속받음 (BurnySC2의 일부분임)
    async def on_step(self, iteration: int): # on_step은 게임의 모든 단계로 불리는 메소드임
        print(f"This is my bot in iteration {iteration}") # 반복되는 번호를 출력함 (즉, step을 출력).


run_game(  # run_game은 게임을 실행하는 함수
    maps.get("2000AtmospheresAIE"), # 우리가 플레이하게 될 맵
    [Bot(Race.Protoss, IncrediBot()), # 코딩한 봇을 실행시킴, 종족은 프로토스, 봇 오브젝트는 생략
     Computer(Race.Zerg, Difficulty.Hard)], # 미리 만들어진 컴퓨터 에이전트를 실행함, 종족은 저그, 어려움 난이도로 설정함
    realtime = False, # 만약 True로 설정한다면, 에이전트는 각 단계가 처리되는데 걸리는 시간이 제한됨
)