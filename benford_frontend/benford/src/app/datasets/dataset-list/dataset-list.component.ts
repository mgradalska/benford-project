import { Component, OnInit } from '@angular/core';

import { ApiService } from '../../api.service';
import { Dataset } from '../dataset.interface';

@Component({
  selector: 'app-dataset-list',
  templateUrl: './dataset-list.component.html',
  styleUrls: ['./dataset-list.component.scss'],
})
export class DatasetListComponent implements OnInit {
  datasets: Dataset[];

  columns: number;

  constructor(private api: ApiService) {}

  ngOnInit() {
    this.api.datasets
      .list()
      .subscribe((datasets) => (this.datasets = datasets));
    this.setBreakpoint(window.innerWidth);
  }

  private setBreakpoint(width) {
    if (width >= 1350) {
      this.columns = 3;
    } else if (width >= 850) {
      this.columns = 2;
    } else {
      this.columns = 1;
    }
  }

  onResize(event) {
    this.setBreakpoint(event.target.innerWidth);
  }
}
