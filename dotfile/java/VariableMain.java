
public class VariableMain {

	public static void main(String[] args) {
		//변수(variable)
		/*
		 * 1. 프로그램에 필요한 데이터를 저장하는 공간
		 * 2. 데이터 타입에 따라 운영체제가 알아서 빈 메모리에 할당 
		 * 
		 * 변수명을 짓는 규칙
		 * 1. 키워드 X (키워드(keyword) : 코드 작성을 위해 미리 정해놓은 단어)
		 * 2. 대소문자 구분 O
		 * 3. 첫글자 : 알파벳, _
		 * 4. 숫자 : 두번째 글자부터 가능
		 * 5. 공백 X
		 * 6. 변수명 중복 X
		 */
		float num1 = 30.3455f;
		double num2 = (double)num1;
		System.out.println(num2);
		num1 = num1+20;
	}

}
