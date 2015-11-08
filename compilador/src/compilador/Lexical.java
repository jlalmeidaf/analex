package compilador;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Lexical {

	public void analysis(String line) {

		Pattern p  = Pattern.compile(".//.*");
		Pattern p2 = Pattern.compile("\b");
		Pattern p3 = Pattern.compile("//.*");
		Pattern p4 = Pattern.compile("^$\n");

		Matcher m   = p.matcher(line);
		Matcher m2  = p2.matcher(line);
		Matcher m3  = p3.matcher(line);
		Matcher m4  = p4.matcher(line);
 

		if (line.isEmpty()) {

			return;
		} else {
			 
				if (m.find()) {
					
					line = line.replaceAll(".//.*", ""); 

				} else if(m2.find()){
					
				}else if(m3.find()) { 
                   line = line.replaceAll("//.*", ""); 
				}
				
				

				System.out.println(line);

		}
		

	}
	
	

}
