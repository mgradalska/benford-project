import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Dataset } from './datasets/dataset.interface';

@Injectable()
export class ApiService {
  constructor(private http: HttpClient) {}

  datasets = {
    list: () => this.http.get<Dataset[]>('api/datasets'),
  };
}
