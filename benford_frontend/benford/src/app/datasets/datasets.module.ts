import { NgModule } from "@angular/core";
import { MatCardModule } from "@angular/material/card";
import { HttpClientModule } from "@angular/common/http";
import { CommonModule } from "@angular/common";
import { MatButtonModule } from "@angular/material/button";
import { MatIconModule } from "@angular/material/icon";
import { MatGridListModule } from "@angular/material/grid-list";
import { MatDialogModule } from "@angular/material/dialog";

import { DatasetListComponent } from "./dataset-list/dataset-list.component";
import { DatasetsRoutingModule } from "./datasets-routing.module";
import { DatasetTileComponent } from "./dataset-tile/dataset-tile.component";
import { DatasetDetailsComponent } from "./dataset-details/dataset-details.component";
import { ApiService } from "../api.service";
import { DatasetAddComponent } from "./dataset-add/dataset-add.component";

@NgModule({
  declarations: [
    DatasetListComponent,
    DatasetTileComponent,
    DatasetDetailsComponent,
    DatasetAddComponent,
  ],
  imports: [
    DatasetsRoutingModule,
    MatCardModule,
    HttpClientModule,
    CommonModule,
    MatButtonModule,
    MatIconModule,
    MatGridListModule,
    MatDialogModule,
  ],
  providers: [ApiService],
})
export class DatasetsModule {}
