import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";

const routes: Routes = [
  {
    path: "",
    redirectTo: "datasets",
    pathMatch: "full",
  },
  {
    path: "datasets",
    loadChildren: () =>
      import("./datasets/datasets.module").then(
        (module) => module.DatasetsModule
      ),
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
