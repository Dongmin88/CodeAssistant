import re
from typing import List, Dict
import json

class CodeAssistant:
    def __init__(self):
        self.command_patterns = {
            'help': r'^help|도움말$',
            'complete': r'^complete|완성\s+(.+)',
            'explain': r'^explain|설명\s+(.+)',
            'fix': r'^fix|수정\s+(.+)',
        }
        
        # 간단한 코드 스니펫 데이터베이스
        self.code_snippets = {
            'python': {
                'for_loop': 'for i in range({}):\n    ',
                'if_statement': 'if {}:\n    ',
                'function': 'def {}():\n    ',
            }
        }
    
    def process_input(self, user_input: str) -> str:
        """사용자 입력을 처리하고 적절한 응답을 반환합니다."""
        for command, pattern in self.command_patterns.items():
            match = re.match(pattern, user_input, re.IGNORECASE)
            if match:
                if command == 'help':
                    return self.show_help()
                elif command == 'complete':
                    return self.complete_code(match.group(1))
                elif command == 'explain':
                    return self.explain_code(match.group(1))
                elif command == 'fix':
                    return self.fix_code(match.group(1))
        
        return "죄송합니다. 명령어를 이해하지 못했습니다. 'help'를 입력하여 사용 가능한 명령어를 확인하세요."

    def show_help(self) -> str:
        """도움말을 표시합니다."""
        return """
사용 가능한 명령어:
- help: 도움말 표시
- complete [코드]: 코드 자동완성 제안
- explain [코드]: 코드 설명
- fix [코드]: 코드 오류 수정 제안
"""

    def complete_code(self, partial_code: str) -> str:
        """코드 자동완성 제안을 제공합니다."""
        # 실제 구현에서는 더 복잡한 로직이 필요합니다
        for lang, snippets in self.code_snippets.items():
            for pattern, completion in snippets.items():
                if pattern in partial_code.lower():
                    return completion.format('')
        return "코드 완성 제안을 찾을 수 없습니다."

    def explain_code(self, code: str) -> str:
        """코드에 대한 설명을 제공합니다."""
        # 실제 구현에서는 더 복잡한 분석 로직이 필요합니다
        return f"제공된 코드의 분석:\n{code}\n기본 설명: 이 코드는..."

    def fix_code(self, code: str) -> str:
        """코드 오류에 대한 수정 제안을 제공합니다."""
        # 실제 구현에서는 더 복잡한 오류 감지 및 수정 로직이 필요합니다
        return f"코드 수정 제안:\n{code}\n수정사항: ..."

# 사용 예시
def main():
    assistant = CodeAssistant()
    print("코드 어시스턴트가 시작되었습니다. 'help'를 입력하여 사용 가능한 명령어를 확인하세요.")
    
    while True:
        user_input = input("\n명령어를 입력하세요 (종료하려면 'quit'): ")
        if user_input.lower() == 'quit':
            break
        
        response = assistant.process_input(user_input)
        print("\n" + response)

if __name__ == "__main__":
    main()