package analizadores;
import java_cup.runtime.Symbol; 


public class Lexico implements java_cup.runtime.Scanner {
	private final int YY_BUFFER_SIZE = 512;
	private final int YY_F = -1;
	private final int YY_NO_STATE = -1;
	private final int YY_NOT_ACCEPT = 0;
	private final int YY_START = 1;
	private final int YY_END = 2;
	private final int YY_NO_ANCHOR = 4;
	private final int YY_BOL = 65536;
	private final int YY_EOF = 65537;
	private java.io.BufferedReader yy_reader;
	private int yy_buffer_index;
	private int yy_buffer_read;
	private int yy_buffer_start;
	private int yy_buffer_end;
	private char yy_buffer[];
	private int yychar;
	private int yyline;
	private boolean yy_at_bol;
	private int yy_lexical_state;

	public Lexico (java.io.Reader reader) {
		this ();
		if (null == reader) {
			throw (new Error("Error: Bad input stream initializer."));
		}
		yy_reader = new java.io.BufferedReader(reader);
	}

	public Lexico (java.io.InputStream instream) {
		this ();
		if (null == instream) {
			throw (new Error("Error: Bad input stream initializer."));
		}
		yy_reader = new java.io.BufferedReader(new java.io.InputStreamReader(instream));
	}

	private Lexico () {
		yy_buffer = new char[YY_BUFFER_SIZE];
		yy_buffer_read = 0;
		yy_buffer_index = 0;
		yy_buffer_start = 0;
		yy_buffer_end = 0;
		yychar = 0;
		yyline = 0;
		yy_at_bol = true;
		yy_lexical_state = YYINITIAL;
 
    yyline = 1; 
    yychar = 1; 
	}

	private boolean yy_eof_done = false;
	private final int YYINITIAL = 0;
	private final int yy_state_dtrans[] = {
		0
	};
	private void yybegin (int state) {
		yy_lexical_state = state;
	}
	private int yy_advance ()
		throws java.io.IOException {
		int next_read;
		int i;
		int j;

		if (yy_buffer_index < yy_buffer_read) {
			return yy_buffer[yy_buffer_index++];
		}

		if (0 != yy_buffer_start) {
			i = yy_buffer_start;
			j = 0;
			while (i < yy_buffer_read) {
				yy_buffer[j] = yy_buffer[i];
				++i;
				++j;
			}
			yy_buffer_end = yy_buffer_end - yy_buffer_start;
			yy_buffer_start = 0;
			yy_buffer_read = j;
			yy_buffer_index = j;
			next_read = yy_reader.read(yy_buffer,
					yy_buffer_read,
					yy_buffer.length - yy_buffer_read);
			if (-1 == next_read) {
				return YY_EOF;
			}
			yy_buffer_read = yy_buffer_read + next_read;
		}

		while (yy_buffer_index >= yy_buffer_read) {
			if (yy_buffer_index >= yy_buffer.length) {
				yy_buffer = yy_double(yy_buffer);
			}
			next_read = yy_reader.read(yy_buffer,
					yy_buffer_read,
					yy_buffer.length - yy_buffer_read);
			if (-1 == next_read) {
				return YY_EOF;
			}
			yy_buffer_read = yy_buffer_read + next_read;
		}
		return yy_buffer[yy_buffer_index++];
	}
	private void yy_move_end () {
		if (yy_buffer_end > yy_buffer_start &&
		    '\n' == yy_buffer[yy_buffer_end-1])
			yy_buffer_end--;
		if (yy_buffer_end > yy_buffer_start &&
		    '\r' == yy_buffer[yy_buffer_end-1])
			yy_buffer_end--;
	}
	private boolean yy_last_was_cr=false;
	private void yy_mark_start () {
		int i;
		for (i = yy_buffer_start; i < yy_buffer_index; ++i) {
			if ('\n' == yy_buffer[i] && !yy_last_was_cr) {
				++yyline;
			}
			if ('\r' == yy_buffer[i]) {
				++yyline;
				yy_last_was_cr=true;
			} else yy_last_was_cr=false;
		}
		yychar = yychar
			+ yy_buffer_index - yy_buffer_start;
		yy_buffer_start = yy_buffer_index;
	}
	private void yy_mark_end () {
		yy_buffer_end = yy_buffer_index;
	}
	private void yy_to_mark () {
		yy_buffer_index = yy_buffer_end;
		yy_at_bol = (yy_buffer_end > yy_buffer_start) &&
		            ('\r' == yy_buffer[yy_buffer_end-1] ||
		             '\n' == yy_buffer[yy_buffer_end-1] ||
		             2028/*LS*/ == yy_buffer[yy_buffer_end-1] ||
		             2029/*PS*/ == yy_buffer[yy_buffer_end-1]);
	}
	private java.lang.String yytext () {
		return (new java.lang.String(yy_buffer,
			yy_buffer_start,
			yy_buffer_end - yy_buffer_start));
	}
	private int yylength () {
		return yy_buffer_end - yy_buffer_start;
	}
	private char[] yy_double (char buf[]) {
		int i;
		char newbuf[];
		newbuf = new char[2*buf.length];
		for (i = 0; i < buf.length; ++i) {
			newbuf[i] = buf[i];
		}
		return newbuf;
	}
	private final int YY_E_INTERNAL = 0;
	private final int YY_E_MATCH = 1;
	private java.lang.String yy_error_string[] = {
		"Error: Internal error.\n",
		"Error: Unmatched input.\n"
	};
	private void yy_error (int code,boolean fatal) {
		java.lang.System.out.print(yy_error_string[code]);
		java.lang.System.out.flush();
		if (fatal) {
			throw new Error("Fatal Error.\n");
		}
	}
	private int[][] unpackFromString(int size1, int size2, String st) {
		int colonIndex = -1;
		String lengthString;
		int sequenceLength = 0;
		int sequenceInteger = 0;

		int commaIndex;
		String workString;

		int res[][] = new int[size1][size2];
		for (int i= 0; i < size1; i++) {
			for (int j= 0; j < size2; j++) {
				if (sequenceLength != 0) {
					res[i][j] = sequenceInteger;
					sequenceLength--;
					continue;
				}
				commaIndex = st.indexOf(',');
				workString = (commaIndex==-1) ? st :
					st.substring(0, commaIndex);
				st = st.substring(commaIndex+1);
				colonIndex = workString.indexOf(':');
				if (colonIndex == -1) {
					res[i][j]=Integer.parseInt(workString);
					continue;
				}
				lengthString =
					workString.substring(colonIndex+1);
				sequenceLength=Integer.parseInt(lengthString);
				workString=workString.substring(0,colonIndex);
				sequenceInteger=Integer.parseInt(workString);
				res[i][j] = sequenceInteger;
				sequenceLength--;
			}
		}
		return res;
	}
	private int yy_acpt[] = {
		/* 0 */ YY_NOT_ACCEPT,
		/* 1 */ YY_NO_ANCHOR,
		/* 2 */ YY_NO_ANCHOR,
		/* 3 */ YY_NO_ANCHOR,
		/* 4 */ YY_NO_ANCHOR,
		/* 5 */ YY_NO_ANCHOR,
		/* 6 */ YY_NO_ANCHOR,
		/* 7 */ YY_NO_ANCHOR,
		/* 8 */ YY_NO_ANCHOR,
		/* 9 */ YY_NO_ANCHOR,
		/* 10 */ YY_NO_ANCHOR,
		/* 11 */ YY_NO_ANCHOR,
		/* 12 */ YY_NO_ANCHOR,
		/* 13 */ YY_NO_ANCHOR,
		/* 14 */ YY_NO_ANCHOR,
		/* 15 */ YY_NO_ANCHOR,
		/* 16 */ YY_NO_ANCHOR,
		/* 17 */ YY_NO_ANCHOR,
		/* 18 */ YY_NO_ANCHOR,
		/* 19 */ YY_NO_ANCHOR,
		/* 20 */ YY_NO_ANCHOR,
		/* 21 */ YY_NO_ANCHOR,
		/* 22 */ YY_NO_ANCHOR,
		/* 23 */ YY_NO_ANCHOR,
		/* 24 */ YY_NO_ANCHOR,
		/* 25 */ YY_NO_ANCHOR,
		/* 26 */ YY_NO_ANCHOR,
		/* 27 */ YY_NO_ANCHOR,
		/* 28 */ YY_NO_ANCHOR,
		/* 29 */ YY_NO_ANCHOR,
		/* 30 */ YY_NO_ANCHOR,
		/* 31 */ YY_NO_ANCHOR,
		/* 32 */ YY_NO_ANCHOR,
		/* 33 */ YY_NO_ANCHOR,
		/* 34 */ YY_NO_ANCHOR,
		/* 35 */ YY_NO_ANCHOR,
		/* 36 */ YY_NO_ANCHOR,
		/* 37 */ YY_NO_ANCHOR,
		/* 38 */ YY_NO_ANCHOR,
		/* 39 */ YY_NO_ANCHOR,
		/* 40 */ YY_NO_ANCHOR,
		/* 41 */ YY_NO_ANCHOR,
		/* 42 */ YY_NO_ANCHOR,
		/* 43 */ YY_NO_ANCHOR,
		/* 44 */ YY_NO_ANCHOR,
		/* 45 */ YY_NO_ANCHOR,
		/* 46 */ YY_NO_ANCHOR,
		/* 47 */ YY_NO_ANCHOR,
		/* 48 */ YY_NOT_ACCEPT,
		/* 49 */ YY_NO_ANCHOR,
		/* 50 */ YY_NO_ANCHOR,
		/* 51 */ YY_NO_ANCHOR,
		/* 52 */ YY_NOT_ACCEPT,
		/* 53 */ YY_NO_ANCHOR,
		/* 54 */ YY_NO_ANCHOR,
		/* 55 */ YY_NOT_ACCEPT,
		/* 56 */ YY_NO_ANCHOR,
		/* 57 */ YY_NOT_ACCEPT,
		/* 58 */ YY_NO_ANCHOR,
		/* 59 */ YY_NOT_ACCEPT,
		/* 60 */ YY_NO_ANCHOR,
		/* 61 */ YY_NOT_ACCEPT,
		/* 62 */ YY_NO_ANCHOR,
		/* 63 */ YY_NOT_ACCEPT,
		/* 64 */ YY_NO_ANCHOR,
		/* 65 */ YY_NOT_ACCEPT,
		/* 66 */ YY_NO_ANCHOR,
		/* 67 */ YY_NOT_ACCEPT,
		/* 68 */ YY_NO_ANCHOR,
		/* 69 */ YY_NOT_ACCEPT,
		/* 70 */ YY_NO_ANCHOR,
		/* 71 */ YY_NOT_ACCEPT,
		/* 72 */ YY_NO_ANCHOR,
		/* 73 */ YY_NOT_ACCEPT,
		/* 74 */ YY_NO_ANCHOR,
		/* 75 */ YY_NOT_ACCEPT,
		/* 76 */ YY_NO_ANCHOR,
		/* 77 */ YY_NOT_ACCEPT,
		/* 78 */ YY_NO_ANCHOR,
		/* 79 */ YY_NOT_ACCEPT,
		/* 80 */ YY_NO_ANCHOR,
		/* 81 */ YY_NOT_ACCEPT,
		/* 82 */ YY_NO_ANCHOR,
		/* 83 */ YY_NOT_ACCEPT,
		/* 84 */ YY_NO_ANCHOR,
		/* 85 */ YY_NOT_ACCEPT,
		/* 86 */ YY_NO_ANCHOR,
		/* 87 */ YY_NOT_ACCEPT,
		/* 88 */ YY_NO_ANCHOR,
		/* 89 */ YY_NOT_ACCEPT,
		/* 90 */ YY_NO_ANCHOR,
		/* 91 */ YY_NOT_ACCEPT,
		/* 92 */ YY_NO_ANCHOR,
		/* 93 */ YY_NOT_ACCEPT,
		/* 94 */ YY_NO_ANCHOR,
		/* 95 */ YY_NOT_ACCEPT,
		/* 96 */ YY_NO_ANCHOR,
		/* 97 */ YY_NOT_ACCEPT,
		/* 98 */ YY_NO_ANCHOR,
		/* 99 */ YY_NOT_ACCEPT,
		/* 100 */ YY_NO_ANCHOR,
		/* 101 */ YY_NOT_ACCEPT,
		/* 102 */ YY_NO_ANCHOR,
		/* 103 */ YY_NOT_ACCEPT,
		/* 104 */ YY_NO_ANCHOR,
		/* 105 */ YY_NOT_ACCEPT,
		/* 106 */ YY_NO_ANCHOR,
		/* 107 */ YY_NOT_ACCEPT,
		/* 108 */ YY_NO_ANCHOR,
		/* 109 */ YY_NOT_ACCEPT,
		/* 110 */ YY_NO_ANCHOR,
		/* 111 */ YY_NOT_ACCEPT,
		/* 112 */ YY_NO_ANCHOR,
		/* 113 */ YY_NOT_ACCEPT,
		/* 114 */ YY_NO_ANCHOR,
		/* 115 */ YY_NOT_ACCEPT,
		/* 116 */ YY_NO_ANCHOR,
		/* 117 */ YY_NOT_ACCEPT,
		/* 118 */ YY_NO_ANCHOR,
		/* 119 */ YY_NOT_ACCEPT,
		/* 120 */ YY_NO_ANCHOR,
		/* 121 */ YY_NOT_ACCEPT,
		/* 122 */ YY_NO_ANCHOR,
		/* 123 */ YY_NOT_ACCEPT,
		/* 124 */ YY_NO_ANCHOR,
		/* 125 */ YY_NOT_ACCEPT,
		/* 126 */ YY_NO_ANCHOR,
		/* 127 */ YY_NOT_ACCEPT,
		/* 128 */ YY_NO_ANCHOR,
		/* 129 */ YY_NOT_ACCEPT,
		/* 130 */ YY_NO_ANCHOR,
		/* 131 */ YY_NO_ANCHOR,
		/* 132 */ YY_NO_ANCHOR,
		/* 133 */ YY_NO_ANCHOR,
		/* 134 */ YY_NO_ANCHOR,
		/* 135 */ YY_NO_ANCHOR,
		/* 136 */ YY_NO_ANCHOR,
		/* 137 */ YY_NO_ANCHOR,
		/* 138 */ YY_NO_ANCHOR,
		/* 139 */ YY_NO_ANCHOR,
		/* 140 */ YY_NO_ANCHOR,
		/* 141 */ YY_NO_ANCHOR,
		/* 142 */ YY_NO_ANCHOR,
		/* 143 */ YY_NO_ANCHOR,
		/* 144 */ YY_NO_ANCHOR,
		/* 145 */ YY_NO_ANCHOR,
		/* 146 */ YY_NOT_ACCEPT,
		/* 147 */ YY_NO_ANCHOR,
		/* 148 */ YY_NOT_ACCEPT,
		/* 149 */ YY_NO_ANCHOR,
		/* 150 */ YY_NO_ANCHOR,
		/* 151 */ YY_NO_ANCHOR,
		/* 152 */ YY_NO_ANCHOR,
		/* 153 */ YY_NO_ANCHOR,
		/* 154 */ YY_NO_ANCHOR,
		/* 155 */ YY_NOT_ACCEPT,
		/* 156 */ YY_NO_ANCHOR,
		/* 157 */ YY_NO_ANCHOR,
		/* 158 */ YY_NOT_ACCEPT,
		/* 159 */ YY_NO_ANCHOR,
		/* 160 */ YY_NO_ANCHOR,
		/* 161 */ YY_NO_ANCHOR,
		/* 162 */ YY_NO_ANCHOR,
		/* 163 */ YY_NO_ANCHOR,
		/* 164 */ YY_NOT_ACCEPT,
		/* 165 */ YY_NO_ANCHOR,
		/* 166 */ YY_NO_ANCHOR,
		/* 167 */ YY_NO_ANCHOR,
		/* 168 */ YY_NO_ANCHOR,
		/* 169 */ YY_NO_ANCHOR,
		/* 170 */ YY_NO_ANCHOR,
		/* 171 */ YY_NO_ANCHOR,
		/* 172 */ YY_NO_ANCHOR,
		/* 173 */ YY_NO_ANCHOR,
		/* 174 */ YY_NO_ANCHOR,
		/* 175 */ YY_NOT_ACCEPT,
		/* 176 */ YY_NOT_ACCEPT,
		/* 177 */ YY_NOT_ACCEPT,
		/* 178 */ YY_NOT_ACCEPT,
		/* 179 */ YY_NOT_ACCEPT,
		/* 180 */ YY_NOT_ACCEPT
	};
	private int yy_cmap[] = unpackFromString(1,65538,
"41:9,33,32,41:2,33,41:18,36,41,38,41:4,40,17,18,24,22,30,23,35,25,34:10,41," +
"16,41:2,31,41:2,3,14,13,7,1,9,29,39,27,39:2,4,12,11,8,26,39,6,10,15,5,2,39:" +
"2,28,39,19,41,20,41,21,41,3,14,13,7,1,9,29,39,27,39:2,4,12,11,8,26,39,6,10," +
"15,5,2,39:2,28,39,41,37,41:65411,0:2")[0];

	private int yy_rmap[] = unpackFromString(1,181,
"0,1,2,1:7,3,1:5,4,5,6:2,1,6,7,6,1:3,6:2,8,9,1,6:6,1,6:4,1:5,10,11,12,13:2,1" +
"4,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,3" +
"9,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,6" +
"4,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,8" +
"9,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110" +
",111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,6,126,127,128," +
"129,130,131,132,133,134,135,136,137,138,139,140")[0];

	private int yy_nxt[][] = unpackFromString(141,42,
"1,2,141,160,165:3,166,49,167,53,168,169,170,171,165,3,4,5,6,7,8,9,10,11,12," +
"172,173,165:2,13,14,15,16,17,14,16,14,50,165,54,14,-1:43,165,174,165:7,56,1" +
"65:5,-1:10,165:4,-1:9,165,-1:33,20,-1:43,16,-1:2,16,-1:39,17,52,-1:7,165:15" +
",-1:10,165:4,-1:9,165,-1:3,165:15,-1:5,71,-1:4,165:4,-1:9,165,-1:3,165:15,-" +
"1:5,89,-1:4,165:4,-1:9,165,-1:3,165:15,-1:5,180,-1:4,165:4,-1:9,165,-1:12,6" +
"3,-1:32,165:5,18,165:9,-1:5,48,-1:4,165:4,-1:9,165,-1:3,55:15,-1:10,55:4,-1" +
":4,55,-1:4,55,-1:36,51,-1,51:2,-1:5,165:15,-1:10,165,19,165:2,-1:9,165,-1:3" +
",57:15,-1:10,57:4,-1:9,57,-1:3,55:15,-1:10,55:4,-1:4,55,-1:3,24,55,-1:3,165" +
":15,-1:5,59,-1:4,165:4,-1:9,165,-1:42,25,-1:2,165:5,144,165:9,-1:10,165:4,-" +
"1:9,165,-1:9,65,-1:19,67,-1:15,165:6,21,165:8,-1:10,165:4,-1:9,165,-1:6,69," +
"-1:38,165:3,86,165:11,-1:10,165:4,-1:9,165,-1:29,26,-1:15,165:10,22,165:4,-" +
"1:10,165:4,-1:9,165,-1:29,75,-1:15,165:11,88,165:3,-1:10,165:4,-1:9,165,-1:" +
"31,77,-1:13,165:14,23,-1:10,165:4,-1:9,165,-1:10,79,-1:34,165:10,145,165:4," +
"-1:10,165:4,-1:9,165,-1:12,81,-1:32,165:15,-1:10,165:2,162,165,-1:9,165,-1:" +
"4,83,-1:40,165:6,90,165:8,-1:10,165:4,-1:9,165,-1:11,85,-1:33,165:5,92,147," +
"165:8,-1:10,165:4,-1:9,165,-1:7,146,-1:37,165:10,161,94,165:3,-1:10,165:4,-" +
"1:9,165,-1:23,87,-1:21,165:7,96,165:7,-1:10,165:4,-1:9,165,-1:29,31,-1:15,1" +
"65:14,163,-1:10,165:4,-1:9,165,-1:5,91,-1:39,165:15,-1:10,165,98,165,100,-1" +
":9,165,-1:3,93,-1:41,165:9,102,165:5,-1:10,165:4,-1:9,165,-1:15,148,-1:29,1" +
"53,165:14,-1:10,165:4,-1:9,165,-1:10,97,-1:34,165:4,151,165:10,-1:10,165:4," +
"-1:9,165,-1:6,99,-1:38,165:2,152,165:12,-1:10,165:4,-1:9,165,-1:8,101,-1:36" +
",165:7,27,165:7,-1:10,165:4,-1:9,165,-1:6,38,-1:38,165:3,110,165:11,-1:10,1" +
"65:4,-1:9,165,-1:23,105,-1:21,165:12,112,165:2,-1:10,165:4,-1:9,165,-1:10,1" +
"07,-1:34,165:5,156,165:9,-1:10,165:4,-1:9,165,-1:3,175,-1:41,165:7,28,165:7" +
",-1:10,165:4,-1:9,165,-1:13,109,-1:31,165:5,29,165:9,-1:10,165:4,-1:9,165,-" +
"1:29,111,-1:15,165:5,30,165:9,-1:10,165:4,-1:9,165,-1:8,43,-1:36,165:10,124" +
",165:4,-1:10,165:4,-1:9,165,-1:17,113,-1:27,157,165:14,-1:10,165:4,-1:9,165" +
",-1:31,115,-1:13,165:15,-1:10,165,128,165:2,-1:9,165,-1:8,119,-1:36,165:2,1" +
"31,165:12,-1:10,165:4,-1:9,165,-1:7,158,-1:37,165:6,132,165:8,-1:10,165:4,-" +
"1:9,165,-1:3,44,-1:41,165:7,32,165:7,-1:10,165:4,-1:9,165,-1:5,121,-1:39,16" +
"5:7,33,165:7,-1:10,165:4,-1:9,165,-1:8,127,-1:36,165:14,159,-1:10,165:4,-1:" +
"9,165,-1:6,45,-1:38,165:2,34,165:12,-1:10,165:4,-1:9,165,-1:6,46,-1:38,165:" +
"12,134,165:2,-1:10,165:4,-1:9,165,-1:29,129,-1:15,165:7,35,165:7,-1:10,165:" +
"4,-1:9,165,-1:10,47,-1:34,165:9,135,165:5,-1:10,165:4,-1:9,165,-1:3,165:5,3" +
"6,165:9,-1:10,165:4,-1:9,165,-1:3,136,165:14,-1:10,165:4,-1:9,165,-1:3,165:" +
"10,37,165:4,-1:10,165:4,-1:9,165,-1:3,165:15,-1:10,165,138,165:2,-1:9,165,-" +
"1:3,165:2,139,165:12,-1:10,165:4,-1:9,165,-1:3,165:5,140,165:9,-1:10,165:4," +
"-1:9,165,-1:3,165:5,39,165:9,-1:10,165:4,-1:9,165,-1:3,165:2,40,165:12,-1:1" +
"0,165:4,-1:9,165,-1:3,165:5,41,165:9,-1:10,165:4,-1:9,165,-1:3,165:7,42,165" +
":7,-1:10,165:4,-1:9,165,-1:3,58,165:14,-1:10,165:4,-1:9,165,-1:3,165:15,-1:" +
"5,61,-1:4,165:4,-1:9,165,-1:3,165:3,149,165:11,-1:10,165:4,-1:9,165,-1:3,16" +
"5:6,150,165:8,-1:10,165:4,-1:9,165,-1:3,165:7,104,165:7,-1:10,165:4,-1:9,16" +
"5,-1:5,95,-1:39,108,165:14,-1:10,165:4,-1:9,165,-1:10,103,-1:34,165:4,114,1" +
"65:10,-1:10,165:4,-1:9,165,-1:3,165:2,116,165:12,-1:10,165:4,-1:9,165,-1:3," +
"165:3,120,165:11,-1:10,165:4,-1:9,165,-1:3,165:12,122,165:2,-1:10,165:4,-1:" +
"9,165,-1:3,165:5,118,165:9,-1:10,165:4,-1:9,165,-1:3,165:10,126,165:4,-1:10" +
",165:4,-1:9,165,-1:17,117,-1:27,130,165:14,-1:10,165:4,-1:9,165,-1:3,165:2," +
"133,165:12,-1:10,165:4,-1:9,165,-1:5,123,-1:39,137,165:14,-1:10,165:4,-1:9," +
"165,-1:3,165:10,60,165:4,-1:10,165:4,-1:9,165,-1:3,165:15,-1:5,73,-1:4,165:" +
"4,-1:9,165,-1:3,165:7,106,165:7,-1:10,165:4,-1:9,165,-1:3,154,165:14,-1:10," +
"165:4,-1:9,165,-1:5,125,-1:39,142,165:14,-1:10,165:4,-1:9,165,-1:3,165:2,62" +
",165:12,-1:10,165,64,165:2,-1:9,165,-1:3,165:4,66,165:2,68,165:7,-1:10,165:" +
"4,-1:9,165,-1:3,70,165,72,165:4,74,165:7,-1:10,165:4,-1:9,165,-1:3,165:2,76" +
",165:4,78,165:7,-1:10,165:4,-1:9,165,-1:3,165:7,80,165:7,-1:10,165:4,-1:9,1" +
"65,-1:3,165:7,82,165:7,-1:10,165:4,-1:9,165,-1:3,165:10,84,165:4,-1:10,165:" +
"4,-1:9,165,-1:3,165:2,143,165:12,-1:10,165:4,-1:9,165,-1:13,155,-1:35,164,-" +
"1:65,176,-1:39,177,-1:35,178,-1:28,179,-1:33");

	public java_cup.runtime.Symbol next_token ()
		throws java.io.IOException {
		int yy_lookahead;
		int yy_anchor = YY_NO_ANCHOR;
		int yy_state = yy_state_dtrans[yy_lexical_state];
		int yy_next_state = YY_NO_STATE;
		int yy_last_accept_state = YY_NO_STATE;
		boolean yy_initial = true;
		int yy_this_accept;

		yy_mark_start();
		yy_this_accept = yy_acpt[yy_state];
		if (YY_NOT_ACCEPT != yy_this_accept) {
			yy_last_accept_state = yy_state;
			yy_mark_end();
		}
		while (true) {
			if (yy_initial && yy_at_bol) yy_lookahead = YY_BOL;
			else yy_lookahead = yy_advance();
			yy_next_state = YY_F;
			yy_next_state = yy_nxt[yy_rmap[yy_state]][yy_cmap[yy_lookahead]];
			if (YY_EOF == yy_lookahead && true == yy_initial) {
				return null;
			}
			if (YY_F != yy_next_state) {
				yy_state = yy_next_state;
				yy_initial = false;
				yy_this_accept = yy_acpt[yy_state];
				if (YY_NOT_ACCEPT != yy_this_accept) {
					yy_last_accept_state = yy_state;
					yy_mark_end();
				}
			}
			else {
				if (YY_NO_STATE == yy_last_accept_state) {
					throw (new Error("Lexical Error: Unmatched Input."));
				}
				else {
					yy_anchor = yy_acpt[yy_last_accept_state];
					if (0 != (YY_END & yy_anchor)) {
						yy_move_end();
					}
					yy_to_mark();
					switch (yy_last_accept_state) {
					case 1:
						
					case -2:
						break;
					case 2:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -3:
						break;
					case 3:
						{return new Symbol(sym.PTCOMA,yyline,yychar, yytext());}
					case -4:
						break;
					case 4:
						{return new Symbol(sym.PARIZQ,yyline,yychar, yytext());}
					case -5:
						break;
					case 5:
						{return new Symbol(sym.PARDER,yyline,yychar, yytext());}
					case -6:
						break;
					case 6:
						{return new Symbol(sym.CORIZQ,yyline,yychar, yytext());}
					case -7:
						break;
					case 7:
						{return new Symbol(sym.CORDER,yyline,yychar, yytext());}
					case -8:
						break;
					case 8:
						{return new Symbol(sym.GBAJO,yyline,yychar, yytext());}
					case -9:
						break;
					case 9:
						{return new Symbol(sym.MAS,yyline,yychar, yytext());}
					case -10:
						break;
					case 10:
						{return new Symbol(sym.MENOS,yyline,yychar, yytext());}
					case -11:
						break;
					case 11:
						{return new Symbol(sym.POR,yyline,yychar, yytext());}
					case -12:
						break;
					case 12:
						{return new Symbol(sym.DIVIDIDO,yyline,yychar, yytext());}
					case -13:
						break;
					case 13:
						{return new Symbol(sym.COMA,yyline,yychar, yytext());}
					case -14:
						break;
					case 14:
						{
    System.out.println("Este es un error lexico: "+yytext()+
    ", en la linea: "+yyline+", en la columna: "+yychar);
}
					case -15:
						break;
					case 15:
						{yychar=1;}
					case -16:
						break;
					case 16:
						{}
					case -17:
						break;
					case 17:
						{return new Symbol(sym.NUMERO,yyline,yychar, yytext());}
					case -18:
						break;
					case 18:
						{return new Symbol(sym.OR,yyline,yychar, yytext());}
					case -19:
						break;
					case 19:
						{return new Symbol(sym.SI,yyline,yychar, yytext());}
					case -20:
						break;
					case 20:
						{return new Symbol(sym.ASIGNACION,yyline,yychar, yytext());}
					case -21:
						break;
					case 21:
						{return new Symbol(sym.AND,yyline,yychar, yytext());}
					case -22:
						break;
					case 22:
						{return new Symbol(sym.FIN,yyline,yychar, yytext());}
					case -23:
						break;
					case 23:
						{return new Symbol(sym.NOT,yyline,yychar, yytext());}
					case -24:
						break;
					case 24:
						{return new Symbol(sym.CADENA,yyline,yychar, yytext());}
					case -25:
						break;
					case 25:
						{return new Symbol(sym.CARACTER,yyline,yychar, yytext());}
					case -26:
						break;
					case 26:
						{return new Symbol(sym.OSI,yyline,yychar, yytext());}
					case -27:
						break;
					case 27:
						{return new Symbol(sym.COMO,yyline,yychar, yytext());}
					case -28:
						break;
					case 28:
						{return new Symbol(sym.FALSO,yyline,yychar, yytext());}
					case -29:
						break;
					case 29:
						{return new Symbol(sym.MENOR,yyline,yychar, yytext());}
					case -30:
						break;
					case 30:
						{return new Symbol(sym.MAYOR,yyline,yychar, yytext());}
					case -31:
						break;
					case 31:
						{return new Symbol(sym.FINSI,yyline,yychar, yytext());}
					case -32:
						break;
					case 32:
						{return new Symbol(sym.TNUMERO,yyline,yychar, yytext());}
					case -33:
						break;
					case 33:
						{return new Symbol(sym.MODULO,yyline,yychar, yytext());}
					case -34:
						break;
					case 34:
						{return new Symbol(sym.TCADENA,yyline,yychar, yytext());}
					case -35:
						break;
					case 35:
						{return new Symbol(sym.INICIO,yyline,yychar, yytext());}
					case -36:
						break;
					case 36:
						{return new Symbol(sym.REVALUAR,yyline,yychar, yytext());}
					case -37:
						break;
					case 37:
						{return new Symbol(sym.TBOOLEAN,yyline,yychar, yytext());}
					case -38:
						break;
					case 38:
						{return new Symbol(sym.ESIGUAL,yyline,yychar, yytext());}
					case -39:
						break;
					case 39:
						{return new Symbol(sym.TCARACTER,yyline,yychar, yytext());}
					case -40:
						break;
					case 40:
						{return new Symbol(sym.POTENCIA,yyline,yychar, yytext());}
					case -41:
						break;
					case 41:
						{return new Symbol(sym.INGRESAR,yyline,yychar, yytext());}
					case -42:
						break;
					case 42:
						{return new Symbol(sym.VERDADERO,yyline,yychar, yytext());}
					case -43:
						break;
					case 43:
						{return new Symbol(sym.CONVALOR,yyline,yychar, yytext());}
					case -44:
						break;
					case 44:
						{return new Symbol(sym.ESDIFERENTE,yyline,yychar, yytext());}
					case -45:
						break;
					case 45:
						{return new Symbol(sym.MENOROIGUAL,yyline,yychar, yytext());}
					case -46:
						break;
					case 46:
						{return new Symbol(sym.MAYOROIGUAL,yyline,yychar, yytext());}
					case -47:
						break;
					case 47:
						{return new Symbol(sym.DELOCONTRARIO,yyline,yychar, yytext());}
					case -48:
						break;
					case 49:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -49:
						break;
					case 50:
						{
    System.out.println("Este es un error lexico: "+yytext()+
    ", en la linea: "+yyline+", en la columna: "+yychar);
}
					case -50:
						break;
					case 51:
						{return new Symbol(sym.NUMERO,yyline,yychar, yytext());}
					case -51:
						break;
					case 53:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -52:
						break;
					case 54:
						{
    System.out.println("Este es un error lexico: "+yytext()+
    ", en la linea: "+yyline+", en la columna: "+yychar);
}
					case -53:
						break;
					case 56:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -54:
						break;
					case 58:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -55:
						break;
					case 60:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -56:
						break;
					case 62:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -57:
						break;
					case 64:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -58:
						break;
					case 66:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -59:
						break;
					case 68:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -60:
						break;
					case 70:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -61:
						break;
					case 72:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -62:
						break;
					case 74:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -63:
						break;
					case 76:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -64:
						break;
					case 78:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -65:
						break;
					case 80:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -66:
						break;
					case 82:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -67:
						break;
					case 84:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -68:
						break;
					case 86:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -69:
						break;
					case 88:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -70:
						break;
					case 90:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -71:
						break;
					case 92:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -72:
						break;
					case 94:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -73:
						break;
					case 96:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -74:
						break;
					case 98:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -75:
						break;
					case 100:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -76:
						break;
					case 102:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -77:
						break;
					case 104:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -78:
						break;
					case 106:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -79:
						break;
					case 108:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -80:
						break;
					case 110:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -81:
						break;
					case 112:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -82:
						break;
					case 114:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -83:
						break;
					case 116:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -84:
						break;
					case 118:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -85:
						break;
					case 120:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -86:
						break;
					case 122:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -87:
						break;
					case 124:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -88:
						break;
					case 126:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -89:
						break;
					case 128:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -90:
						break;
					case 130:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -91:
						break;
					case 131:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -92:
						break;
					case 132:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -93:
						break;
					case 133:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -94:
						break;
					case 134:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -95:
						break;
					case 135:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -96:
						break;
					case 136:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -97:
						break;
					case 137:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -98:
						break;
					case 138:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -99:
						break;
					case 139:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -100:
						break;
					case 140:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -101:
						break;
					case 141:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -102:
						break;
					case 142:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -103:
						break;
					case 143:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -104:
						break;
					case 144:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -105:
						break;
					case 145:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -106:
						break;
					case 147:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -107:
						break;
					case 149:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -108:
						break;
					case 150:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -109:
						break;
					case 151:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -110:
						break;
					case 152:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -111:
						break;
					case 153:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -112:
						break;
					case 154:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -113:
						break;
					case 156:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -114:
						break;
					case 157:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -115:
						break;
					case 159:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -116:
						break;
					case 160:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -117:
						break;
					case 161:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -118:
						break;
					case 162:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -119:
						break;
					case 163:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -120:
						break;
					case 165:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -121:
						break;
					case 166:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -122:
						break;
					case 167:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -123:
						break;
					case 168:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -124:
						break;
					case 169:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -125:
						break;
					case 170:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -126:
						break;
					case 171:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -127:
						break;
					case 172:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -128:
						break;
					case 173:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -129:
						break;
					case 174:
						{return new Symbol(sym.NOMBRE,yyline,yychar, yytext());}
					case -130:
						break;
					default:
						yy_error(YY_E_INTERNAL,false);
					case -1:
					}
					yy_initial = true;
					yy_state = yy_state_dtrans[yy_lexical_state];
					yy_next_state = YY_NO_STATE;
					yy_last_accept_state = YY_NO_STATE;
					yy_mark_start();
					yy_this_accept = yy_acpt[yy_state];
					if (YY_NOT_ACCEPT != yy_this_accept) {
						yy_last_accept_state = yy_state;
						yy_mark_end();
					}
				}
			}
		}
	}
}
