#pragma once
#include <vector>

using vector_float = std::vector<std::vector<float>>;

//���������� �������� ������� 2x2
vector_float reverse(vector_float A);

// ������� ���������� ������ X � V
vector_float formula_XV(vector_float M, vector_float N, vector_float Q1, vector_float P);

// ��������� ������� 2x2
vector_float mul(vector_float C, vector_float N, vector_float Q1);

// ������� ���������� ������ U � Y
vector_float formula_UY(vector_float V, vector_float P, vector_float M1);

// ������� ��������� ������ ��� ������
vector_float memoVector(vector_float A, unsigned n, unsigned m);

// ����� �� ����� ������� 2�2
void printVector(vector_float A);

// ����� �� ����� ������� 4�4, ���� 4 ������� 2�2
void printMatrix(vector_float X, vector_float Y, vector_float U, vector_float V);