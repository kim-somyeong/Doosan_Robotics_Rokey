from ros2cli.command import add_subparsers_on_demand
from ros2cli.command import CommandExtension

class EnvCommand(CommandExtension):
    def add_arguments(self, parser, cli_name):
        self._subparser = parser

        #add arguments and sub-commands of verbs
        add_subparsers_on_demand(
            parser, cli_name, "_verb", "ros2env.verb", required=False
        )

    def main(self, *, parser, args):
        if not hasattr(args, "_verb"):
            #서브 명령어가 전달되지 않았을 때, 도움말을 출력
            self._subparser.print_help()
            return 0
        
        #속성 '_verb'를 기준으로 서브 명령어(verb)를 가져옴
        extension = getattr(args, "_verb")

        #해당 서브 명령어의 main 메서드를 호출하여 실행
        return extension.main(args=args)