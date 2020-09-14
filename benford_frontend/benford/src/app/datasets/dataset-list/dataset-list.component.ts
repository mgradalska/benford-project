import { Component, OnInit } from "@angular/core";
import { MatDialog } from "@angular/material/dialog";
import { Router } from "@angular/router";

import { filter } from "rxjs/operators";

import { ApiService } from "../../api.service";
import { Dataset } from "../dataset.interface";
import { DatasetAddComponent } from "../dataset-add/dataset-add.component";

@Component({
  selector: "app-dataset-list",
  templateUrl: "./dataset-list.component.html",
  styleUrls: ["./dataset-list.component.scss"],
})
export class DatasetListComponent implements OnInit {
  datasets: Dataset[];

  columns: number;

  constructor(
    private api: ApiService,
    private dialog: MatDialog,
    private router: Router
  ) {}

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

  openDialog() {
    const dialog = this.dialog.open(DatasetAddComponent, {
      width: "500px",
    });

    dialog
      .afterClosed()
      .pipe(filter((result) => !!result))
      .subscribe((createdDataset: Dataset) =>
        this.router.navigate([`datasets/${createdDataset.id}/`])
      );
  }
}
