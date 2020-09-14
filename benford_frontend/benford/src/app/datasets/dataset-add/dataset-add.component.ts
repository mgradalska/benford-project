import { Component } from "@angular/core";
import { MatDialogRef } from "@angular/material/dialog";

import { ApiService } from "../../api.service";
import { Dataset } from "../dataset.interface";

@Component({
  selector: "app-dataset-add",
  templateUrl: "./dataset-add.component.html",
  styleUrls: ["./dataset-add.component.scss"],
})
export class DatasetAddComponent {
  file: File;

  error: string;

  constructor(
    private api: ApiService,
    private dialog: MatDialogRef<DatasetAddComponent>
  ) {}

  handleFileInput(files: FileList) {
    this.file = files.item(0);
  }

  submitFile() {
    const formData = new FormData();
    formData.append("file", this.file);

    this.api.datasets.create(formData).subscribe(
      (createdDataset: Dataset) => this.dialog.close(createdDataset),
      (error) => (this.error = error.error)
    );
  }
}
