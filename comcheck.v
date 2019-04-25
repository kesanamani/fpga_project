
module check(input wire clk,input wire reset,input wire signed[8:0] sig, output reg signed[18:0] filter_out, output reg out_sig);

reg signed[20:0] w[9:0];
reg signed[3:0] i;
reg signed[8:0] img[10:0];
reg signed[3:0] j;
reg signed[31:0] temp;
reg signed[28:0] temp1;
initial begin
out_sig <= 1'b0;
filter_out <= 16'd0;

w[1] <= -21'd95003;
w[2] <= -21'd117939;
w[3] <= 21'd52036;
w[4] <= -21'd55799;
w[5] <= -21'd37860;
w[6] <= 21'd224943;
w[7] <= 21'd150578;
w[8] <= 21'd247485;
w[9] <= 21'd611424;

//~ w[0] <= 21'd1;
//~ w[1] <= 21'd1000;
//~ w[2] <= 21'd1000;
//~ w[3] <= 21'd1000;
//~ w[4] <= 21'd1000;
//~ w[5] <= 21'd1000;
//~ w[6] <= 21'd1000;
//~ w[7] <= 21'd1000;
//~ w[8] <= 21'd1000;
//~ w[9] <= 21'd1000;
end

always@ (posedge clk  )
begin  
	out_sig = 0;
	if(reset==1) begin
		img[j] = sig;
		j = j + 4'd1;
		if(j == 4'd10)
		begin
			j = 4'd0;
			temp = 31'd0;
			//~ temp = img[1] +img[2] + img[3]+ img[4]+ img[5]+ img[6]+ img[7] + img[8] +img[9];
			
			temp = img[1]*w[1] +img[2]*w[2] + img[3]*w[3] + img[4]*w[4] + img[5]*w[5] + img[6]*w[6] + img[7]*w[7] + img[8]*w[8]+ img[9]*w[9]; 
			
			//~ + img[3]*w[3] + img[4]*w[4] + img[5]*w[5] + img[6]*w[6] + img[7]*w[7] + img[8]*w[8]+ img[9]*w[9];
			
			//~ temp = 31'd9000;
			//~ filter_out = img[9];
			filter_out=temp[28:10];
			out_sig = 1;
		end
		
	end
	if(reset==0) begin
		j=4'd0;
		filter_out =16'd0;
		
		temp=31'd0;
		img[0]=9'd0;
		img[1]=9'd0;
		img[2]=9'd0;
		img[3]=9'd0;
		img[4]=9'd0;
		img[5]=9'd0;
		img[6]=9'd0;
		img[7]=9'd0;
		img[8]=9'd0;
		img[9]=9'd0;
		img[10]=9'd0;
		//~ filter_out = 16'd2;
	end
	
	//filter_out <= (temp1>>14);
	//filter_out <= temp;
	//out_sig <= 1'b1;
	//out_sig <= 1'b0;
end
endmodule
	
