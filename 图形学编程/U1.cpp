#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
#include<math.h> 
#include "atltypes.h"
//#include "afxwin.h"

//DDA�㷨��ֱ��
void DrawLine1(CPoint start,CPoint end)
{
	int x1 = start.x,y1 = start.y;
	int x2 = end.x,y2 =end.y;
	int i;
	float dx,dy,length;
	float x=float(x1),y=float(y1);
	//CClientDC dc(this);
//	HDC dc;
//	CClientDC dc(this);

	//����ֱ�߳��� 
	//CDC* pDC = GetDlgItem(IDC_)->GetDC();
//������ǰ��Ļ��
	HDC DC = GetWindowDC(GetDesktopWindow());
	if(fabs(x2-x1)>= fabs(y2-y1))
		length=float(fabs(x2-x1));
	else
		length=float(fabs(y2-y1));
		
	dx=(x2-x1)/length;
	dy=(y2-y1)/length;
	
	//��ֱ��
	for(i=0;i<=length;i++)
	{
		SetPixel(DC,int(x+0.5),int(y+0.5),RGB(0,255,0));
		x+=dx;
		y+=dy;
	 } 
	//system("pause");
 } 

//Bersheman�㷨��ֱ��
void DrawLine2(CPoint start, CPoint end)
{
	int x1 = start.x, x2 = end.x;
	int y1 = start.y, y2 = end.y;
	int dx = x2 - x1, dy = y2 - y1;
	int e = -dx;
	int x = x1, y = y1;
	HDC DC = GetWindowDC(GetDesktopWindow());
	for (int i = 0;i<dx;i++)
	{
		SetPixel(DC, int(x), int(y), RGB(0, 0, 205));
		if (e >= 0)
		{
			y = y + 1;
			e = e - 2 * dx;
		}
		x = x + 1;
		e = e + 2 * dy;

	}

}

void CirclePoints(int x0, int y0, int x, int y)
{
	HDC DC = GetWindowDC(GetDesktopWindow());
	SetPixel(DC, int(x0 + x), int(y0 + y), RGB(0, 100, 0));
	SetPixel(DC, int(x0 + y), int(y0 + x), RGB(0, 100, 0));
	SetPixel(DC, int(x0 - x), int(y0 + y), RGB(0, 100, 0));
	SetPixel(DC, int(x0 + y), int(y0 - x), RGB(0, 100, 0));
	SetPixel(DC, int(x0 + x), int(y0 - y), RGB(0, 100, 0));
	SetPixel(DC, int(x0 - y), int(y0 - x), RGB(0, 100, 0));
	SetPixel(DC, int(x0 - x), int(y0 - y), RGB(0, 100, 0));
	SetPixel(DC, int(x0 - y), int(y0 + x), RGB(0, 100, 0));
}

//bershmanԲ��

void DrawArch(int x0,int y0,int r)
{
	int x, y, d;
	x = 0, y = r, d = 3 - 2 * r;
	//HDC DC = GetWindowDC(GetDesktopWindow());
	while (x < y)
	{
		//SetPixel(DC, int(x), int(y), RGB(0, 100, 0));
		CirclePoints(x0, y0, x, y);
		if (d < 0)
		{
			d = d + 4 * x + 6;
		}
		else
		{
			d = 4 * (x - y) + 10;
			y = y - 1;
		}
		x = x + 1;
	}
	/*if (x == y)
	{
		SetPixel(DC, int(x), int(y), RGB(0, 100, 0));
	}*/
}

//��������Բ��
void DrawCircle2(int x0, int y0, int r)
{
	int x = 0, y = r, f = 0;
	while (y >0) {
		CirclePoints(x0, y0, x, y);
		if (f > 0) {
			f = f - 2 * (y) + 1;
			y--;

		}
		else {
			f =f- 2 * (x) + 1;
			x++;

		}
	}
	/*if (y == y0)
	{
		CirclePoints(x0, y0, x, y);
	}*/
}

//����αƽ�����Բ��
//Ϊʲôֻ�ܻ�����Բ����
#define PI 3.1415926
void DrawCircle3(int x0, int y0, int r)
{
	double x = float(r), y = float(0);
	double dx = sin(PI / 24), dy = cos(PI / 24);
	double temp1,temp2;
	int i;
	for (i = 0; i <= 48; i++)
	{
		temp1 = x;
		temp2 = y;
		x = temp1*dy - temp2*dx;
		y = temp1*dx + temp2*dy;
		CPoint start,end;
		start.x = int(temp1 + 0.5 + x0);
		start.y =int(temp2 + 0.5 + y0);
		end.x =  int(x + 0.5 + x0);
		end.y = int(y + 0.5 + y0);
		DrawLine2(start, end);

	}
}

//��Բ����
void DrawEllipase(int x0, int y0,int a, int b)
{
	int aa = a*a, bb = b*b;
	int x = 0, y = b;
	int d = (int)(bb + aa*(0.25 - b) + 0.5);
	int dx = 0, dy = 2 * aa*y;
	HDC DC = GetWindowDC(GetDesktopWindow());
	//�ĸ���
	SetPixel(DC, int(x0 + x), int(y0 + y), RGB(0, 100, 0));
	SetPixel(DC, int(x0 + x), int(y0 - y), RGB(0, 100, 0));
	SetPixel(DC, int(x0 - x), int(y0 + y), RGB(0, 100, 0));
	SetPixel(DC, int(x0 - x), int(y0 - y), RGB(0, 100, 0));
	//��Բ�ϰ벿��
	while (dx < dy)
	{
		x++;
		dx += 2 * bb;
		if (d < 0)
			d += bb + dx;
		else
		{
			dy -= 2 * aa;
			d += bb + dx - dy;
			y--;
		}
		SetPixel(DC, int(x0 + x), int(y0 + y), RGB(0, 100, 0));
		SetPixel(DC, int(x0 + x), int(y0 - y), RGB(0, 100, 0));
		SetPixel(DC, int(x0 - x), int(y0 + y), RGB(0, 100, 0));
		SetPixel(DC, int(x0 - x), int(y0 - y), RGB(0, 100, 0));

	}
	d = (int)(bb*(x + 0.5)*(x + 0.5) + aa*(y - 1)*(y - 1) - aa*bb + 0.5);
	while (y > 0)
	{
		y--;
		dy -= 2 * aa;
		if (d > 0)
			d += aa - dy;
		else
		{
			dx += 2 * bb;
			d += aa - dy + dx;
			x++;
		}
		SetPixel(DC, int(x0 + x), int(y0 + y), RGB(0, 100, 0));
		SetPixel(DC, int(x0 + x), int(y0 - y), RGB(0, 100, 0));
		SetPixel(DC, int(x0 - x), int(y0 + y), RGB(0, 100, 0));
		SetPixel(DC, int(x0 - x), int(y0 - y), RGB(0, 100, 0));
	}
}

//�������Ӱ���

//�������ɫ���


//https://wenku.baidu.com/view/eeae8ea7284ac850ad02426a.html
 
 int main()
 {
	 CPoint start;
	 CPoint end;
 	start.x=100;
 	start.y=200;
	//HDC DC=GetWindowDC(GetDesktopWindow());
 	end.x=700;
 	end.y=800;
 	//DrawLine1(start,end);//DDAֱ��
	//DrawLine2(start, end);//Bershmanֱ��
	//DrawArch(100,200,100);//BershmanԲ��
	//DrawCircle2(200, 300, 100);//����Բ��
	//DrawCircle3(300, 400, 200);//����αƽ�Բ��
	DrawEllipase(400, 500, 200, 100);//��Բ
	system("pause");
  } 
