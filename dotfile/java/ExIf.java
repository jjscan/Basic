			import java.util.Random;
			
			
			public class ExIf {
			
				public static void main(String[] args) {
					// TODO Autogenerated method stub
					Random r = new Random();
				
					int score = r.nextInt(101);//0~100
					
					/*
					 * 90 ~ 100 성적 등급 A
					 *  80 ~ 89 성적 등급 B
					 *  70 ~ 79 성적 등급 C
					 *  60 ~ 69 성적 등급 D
					 *  00 ~ 59 성적 등급 F
					 */
					
					if(score >= 90) {
						System.out.println("성적등급 A");
					}else if(score >= 80 ) {
						System.out.println("성적등급 B");
					}else if(score >= 70) {
						System.out.println("성적등급 C");
					}else if(score >= 60) {
						System.out.println("성적등급 D");
					}else {
						System.out.println("성적등급 F");
					}
				}
			
			}
