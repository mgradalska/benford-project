import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DatasetListComponent } from './dataset-list/dataset-list.component';
import { DatasetDetailsComponent } from './dataset-details/dataset-details.component';

const routes: Routes = [
  {
    path: '',
    component: DatasetListComponent,
  },
  {
    path: ':id',
    component: DatasetDetailsComponent,
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DatasetsRoutingModule {}
