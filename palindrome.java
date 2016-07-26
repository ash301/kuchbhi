import java.io.*;
import java.util.*;

class palindrome 
{
	palindrome()
	{	
			
		String original , reverse="";
		int l;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		//take the input

		try
	{
		original = br.readLine();
		l=original.length();

		for(int i=l-1;i>=0;i--)
		{
			reverse = reverse + original.charAt(i);
		}

		if(original.equals(reverse))
		{
			System.out.println("palindrome");

		}

		else
			System.out.println("not palindrome");


	}catch(IOException e){}

}


	public static void main(String[] args) throws IOException{
		
		palindrome ob = new palindrome();

	}
}