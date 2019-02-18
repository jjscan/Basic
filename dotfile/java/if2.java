

			public class if2 {
			
				public static void main(String[] args) {
					// TODO Auto-generated method stub
					char ch = 'A';
					
					if(ch >= 'A' && ch <= 'Z') {
						System.out.println("저장된 글자는 대문자 입니다.");
					}else if(ch >='a' && ch <= 'z') {
						System.out.println("저장된 글자는 소문자 입니다.");
					}else {
						System.out.println("이 글자는 알파벳이 아닙니다.");			
					}
				}
			
			}
