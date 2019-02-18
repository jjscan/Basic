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
		System.out.println("Че ="+sum(a,b)); //Че
		System.out.println("ЦђБе="+avg(a,b));
		float av = avg(a,b);//ЦђБе
		grade(av);
		sum(a,b); //Че
		avg(a,b); //ЦђБе
	}

}
