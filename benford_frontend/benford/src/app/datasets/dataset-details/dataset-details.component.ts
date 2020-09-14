import { Component, OnInit } from "@angular/core";
import { ActivatedRoute } from "@angular/router";

import { Dataset } from "../dataset.interface";
import { ApiService } from "../../api.service";

@Component({
  selector: "app-dataset-details",
  templateUrl: "./dataset-details.component.html",
  styleUrls: ["./dataset-details.component.scss"],
})
export class DatasetDetailsComponent implements OnInit {
  dataset: Dataset;

  constructor(private route: ActivatedRoute, private api: ApiService) {}

  ngOnInit() {
    const datasetId = +this.route.snapshot.paramMap.get("id");
    this.api.datasets
      .get(datasetId)
      .subscribe((dataset) => (this.dataset = dataset));
  }
}
