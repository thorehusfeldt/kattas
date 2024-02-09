import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class StringModification {
    public static void main(String[] args) throws IOException {
	BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String s = reader.readLine();
        char[] l = s.toCharArray();
        char bit = '0';
        for (int i = 0; i < l.length; i++) {
            if (l[i] == 'b') {
                l[i] = bit;
                bit = (bit == '0') ? '1' : '0';
            }
        }
        System.out.println(new String(l));
    }
}
