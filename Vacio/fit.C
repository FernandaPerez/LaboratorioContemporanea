#include <stdio.h>
#include <TFile.h>
#include <TGraph.h>
#include <TF1.h>
#include <TTree.h>
#include <TVector.h>
#include <iostream>
#include <fstream>
#include <string>
#include <TColor.h>
#include <TMath.h>

int NumberOfLines(ifstream &file){
  int LinesCont = 0;
  string unused;
  while(getline(file, unused)){
    ++LinesCont;
  }
  file.clear();
  file.seekg(0);

  return LinesCont;

}




void fit(){
  //int NumberOfLines();
  string input_name;
  cout << "Archivo de datos sin extension \n";
  cin >>  input_name;



  //const char *input_name = "para_grafica";
  string name = input_name+".txt";
  cout << name;
  ifstream file(name.c_str());

if (!file) {
  cout << "Archivo no encontado \n";
}
else{
  int N_Lines = NumberOfLines(file);
  printf("Number of lines: %i \n", N_Lines);

  int j = 0;
  float t, P;

  //int LinesCont = NumberOfLines(archivo);

   TVectorD X(N_Lines+1);
   TVectorD Y(N_Lines+1);

  while (!file.eof()){
    file >> t >> P;
    printf("%i, %f, %f \n", j, t, P);
    //getchar();

    X(j) = t;
    Y(j) = P;

    ++j;

  }
  TCanvas *Grafico = new TCanvas("Grafico", "Grafico de P contra t", 200, 10, 700, 500);
  TGraph *gr = new TGraph(X,Y);

  TF1 *f = new TF1 ("fit", FitFunction, 80, 2000, 2);
  f -> SetParameters(700, 0.5);
  f -> SetParNames("PresionControl", "VelocidadEfectiva");
  f ->SetLineStyle(1);
  f ->SetLineColor(kBlue);
  gr -> Fit("fit", "R");

  gr->SetMarkerColor(kPink - 9);

  gr->SetMarkerStyle(23);
  gr->SetMarkerSize(0.5);
  gr->SetTitle("P(t) vs t");
  gr->GetXaxis()->SetTitle("Tiempo (s)");
  gr->GetYaxis()->SetTitle("Presion (Torr)");
  gr->GetYaxis()->SetRange(-100, 800);
  gr->Draw("AP");

  leg = new TLegend(0.69,0.74,0.88,0.88);
  leg->SetHeader("Muestra");
  leg->AddEntry("f",Form("P=P_{0} e^{%f t/V}", f->GetParameter(1)), "l");
  leg->AddEntry("gr","P(t)","lep");
  leg->Draw();

  //Grafico.SetLogy();
  Grafico->Update();
  string save_file = input_name+".png";
  Grafico->Print(save_file.c_str());
  //printf("%i", cont);
}


  cout << "Funciona" << endl;
  Hola();

}

Double_t FitFunction (Double_t *x, Double_t *par){
  Double_t fitval = 760.0*TMath::Exp((-par[1]/14.55)*x[0]);
  return fitval;

}


void Hola(){
  cout << "hola" << endl;
}
