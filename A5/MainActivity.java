package com.example.dm.myapplication;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private Button btn0;
    private Button btn1;
    private Button btn2;
    private Button btn3;
    private Button btn4;
    private Button btn5;
    private Button btn6;
    private Button btn7;
    private Button btn8;
    private Button btn9;
    private Button btnadd;
    private Button btnsub;
    private Button btndiv;
    private Button btnmul;
    private Button btnclear;
    private Button btnequal;
    private Button btnsin;
    private Button btncos;
    private Button btntan;
    private Button btnsqr;
    private TextView info;
    private TextView result;
    private double val1=Double.NaN;
    private double val2=Double.NaN;
    private char Operation=0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        setUpUIViews();

        btn0.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                info.setText(info.getText().toString() + "0");
            }
        });
        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                info.setText(info.getText().toString() + "1");
            }
        });
        btn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                info.setText(info.getText().toString() + "2");
            }
        });
        btn3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                info.setText(info.getText().toString() + "3");
            }
        });
        btn4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                info.setText(info.getText().toString() + "4");
            }
        });
        btn5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                info.setText(info.getText().toString() + "5");
            }
        });
        btn6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                info.setText(info.getText().toString() + "6");
            }
        });
        btn7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                info.setText(info.getText().toString() + "7");
            }
        });
        btn8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                info.setText(info.getText().toString() + "8");
            }
        });
        btn9.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                info.setText(info.getText().toString() + "9");
            }
        });

        btnadd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                compute();
                Operation='+';
                result.setText(String.valueOf(val1) + "+");
                info.setText(null);
            }
        });
        btnsub.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                compute();
                Operation='-';
                result.setText(String.valueOf(val1) + "-");
                info.setText(null);
            }
        });
        btnmul.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                compute();
                Operation='*';
                result.setText(String.valueOf(val1) + "*");
                info.setText(null);
            }
        });
        btndiv.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                compute();
                Operation='/';
                result.setText(String.valueOf(val1) + "/");
                info.setText(null);
            }
        });
        btnequal.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                compute();
                if (Operation=='1'|| Operation=='2' || Operation=='3'|| Operation=='4' ){
                    compute();
                    result.setText(result.getText().toString()+String.valueOf(val1) + " = "+String.valueOf(val2));
                }
                else {
                    result.setText(result.getText().toString() + String.valueOf(val2) + "=" + String.valueOf(val1));
                }
                info.setText(null);
                Operation='=';
            }
        });
        btnclear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                info.setText(null);
                result.setText(null);
                val1=Double.NaN;
                val2=Double.NaN;
            }
        });

        btnsin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                result.setText("Sin ");
                Operation='1';
            }
        });
        btncos.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                result.setText("Cos ");
                Operation='2';
            }
        });
        btntan.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                result.setText("Tan ");
                Operation='3';
            }
        });
        btnsqr.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //compute();
                result.setText("SQR ");
                Operation='4';
            }
        });
    }
    private void setUpUIViews(){
        btn0=(Button)findViewById(R.id.btn0);
        btn1=(Button)findViewById(R.id.btn1);
        btn2=(Button)findViewById(R.id.btn2);
        btn3=(Button)findViewById(R.id.btn3);
        btn4=(Button)findViewById(R.id.btn4);
        btn5=(Button)findViewById(R.id.btn5);
        btn6=(Button)findViewById(R.id.btn6);
        btn7=(Button)findViewById(R.id.btn7);
        btn8=(Button)findViewById(R.id.btn8);
        btn9=(Button)findViewById(R.id.btn9);
        btnadd=(Button)findViewById(R.id.btnadd);
        btnsub=(Button)findViewById(R.id.btnsub);
        btndiv=(Button)findViewById(R.id.btndiv);
        btnmul=(Button)findViewById(R.id.btnmul);
        btnclear=(Button)findViewById(R.id.btnclear);
        btnequal=(Button)findViewById(R.id.btnequal);
        info=(TextView)findViewById(R.id.tvControl);
        result=(TextView)findViewById(R.id.tvResult);

        btnsin=(Button)findViewById(R.id.btsin);
        btncos=(Button)findViewById(R.id.btcos);
        btntan=(Button)findViewById(R.id.bttan);
        btnsqr=(Button)findViewById(R.id.btsq);
    }
    private void compute(){
        if(Double.isNaN(val1)){
            val1=Double.parseDouble(info.getText().toString());
        }
        else {
            val2=Double.parseDouble(info.getText().toString());
            switch(Operation){
                case '+':
                    val1=val1+val2;
                    break;
                case '-':
                    val1=val1-val2;
                    break;
                case '*':
                    val1=val1*val2;
                    break;
                case '/':
                    val1=val1/val2;
                    break;
                case '1':
                    val1=Math.toRadians(val1);
                    val2=Math.sin(val1);
                    break;
                case '2':
                    val1=Math.toRadians(val1);
                    val2=Math.cos(val1);
                    break;
                case '3':
                    val1=Math.toRadians(val1);
                    val2=Math.tan(val1);
                    break;
                case '4':
                    val2=Math.sqrt(val1);
                    break;
                case '=':
                    break;

            }
        }
    }
}
