import java.util.Scanner;

public class FunctionTest {

public static int sum(int x, int y) {
	
	int s = x + y;
	return s;
	
}
public static float avg(float x,float y) {
	
	float w = (float)(x + y)/2;
	return w;
	
}

public static void grade(float x, float y)

	float e = (int)

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		System.out.println("�� ="+sum(a,b)); //��
		System.out.println("���="+avg(a,b));
		float av = avg(a,b);//���
		grade(av);
		sum(a,b); //��
		avg(a,b); //���
	}

}
