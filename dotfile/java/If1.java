import java.util.Random;



public class If1 {
				
					public static void main(String[] args) {
						// TODO Auto-generated method stub
						Random r = new Random();
						int num = r.nextInt();
						
						//num이 3의 배수이거나 4의 배수이면 화면에 출력
						if(num % 3 == 0 || num % 4 == 0) {
							System.out.println("이"+num+"숫자는 3의 또는 4의 배수 입니다.");
						}else {
							System.out.println("이"+num+"숫자는 3의 또는 4의 배수가 아닙니다.");
						}
						System.out.println(num);
					}
				
				}
