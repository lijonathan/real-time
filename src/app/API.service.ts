/* tslint:disable */
/* eslint-disable */
//  This file was automatically generated and should not be edited.
import { Injectable } from "@angular/core";
import API, { graphqlOperation } from "@aws-amplify/api";
import { GraphQLResult } from "@aws-amplify/api/lib/types";
import * as Observable from "zen-observable";

export type CreateMyTypeInput = {
  id?: string | null;
  title: string;
  content: string;
  price?: number | null;
  rating?: number | null;
};

export type ModelMyTypeConditionInput = {
  title?: ModelStringInput | null;
  content?: ModelStringInput | null;
  price?: ModelIntInput | null;
  rating?: ModelFloatInput | null;
  and?: Array<ModelMyTypeConditionInput | null> | null;
  or?: Array<ModelMyTypeConditionInput | null> | null;
  not?: ModelMyTypeConditionInput | null;
};

export type ModelStringInput = {
  ne?: string | null;
  eq?: string | null;
  le?: string | null;
  lt?: string | null;
  ge?: string | null;
  gt?: string | null;
  contains?: string | null;
  notContains?: string | null;
  between?: Array<string | null> | null;
  beginsWith?: string | null;
  attributeExists?: boolean | null;
  attributeType?: ModelAttributeTypes | null;
  size?: ModelSizeInput | null;
};

export enum ModelAttributeTypes {
  binary = "binary",
  binarySet = "binarySet",
  bool = "bool",
  list = "list",
  map = "map",
  number = "number",
  numberSet = "numberSet",
  string = "string",
  stringSet = "stringSet",
  _null = "_null"
}

export type ModelSizeInput = {
  ne?: number | null;
  eq?: number | null;
  le?: number | null;
  lt?: number | null;
  ge?: number | null;
  gt?: number | null;
  between?: Array<number | null> | null;
};

export type ModelIntInput = {
  ne?: number | null;
  eq?: number | null;
  le?: number | null;
  lt?: number | null;
  ge?: number | null;
  gt?: number | null;
  between?: Array<number | null> | null;
  attributeExists?: boolean | null;
  attributeType?: ModelAttributeTypes | null;
};

export type ModelFloatInput = {
  ne?: number | null;
  eq?: number | null;
  le?: number | null;
  lt?: number | null;
  ge?: number | null;
  gt?: number | null;
  between?: Array<number | null> | null;
  attributeExists?: boolean | null;
  attributeType?: ModelAttributeTypes | null;
};

export type UpdateMyTypeInput = {
  id: string;
  title?: string | null;
  content?: string | null;
  price?: number | null;
  rating?: number | null;
};

export type DeleteMyTypeInput = {
  id?: string | null;
};

export type ModelMyTypeFilterInput = {
  id?: ModelIDInput | null;
  title?: ModelStringInput | null;
  content?: ModelStringInput | null;
  price?: ModelIntInput | null;
  rating?: ModelFloatInput | null;
  and?: Array<ModelMyTypeFilterInput | null> | null;
  or?: Array<ModelMyTypeFilterInput | null> | null;
  not?: ModelMyTypeFilterInput | null;
};

export type ModelIDInput = {
  ne?: string | null;
  eq?: string | null;
  le?: string | null;
  lt?: string | null;
  ge?: string | null;
  gt?: string | null;
  contains?: string | null;
  notContains?: string | null;
  between?: Array<string | null> | null;
  beginsWith?: string | null;
  attributeExists?: boolean | null;
  attributeType?: ModelAttributeTypes | null;
  size?: ModelSizeInput | null;
};

export type CreateMyTypeMutation = {
  __typename: "MyType";
  id: string;
  title: string;
  content: string;
  price: number | null;
  rating: number | null;
};

export type UpdateMyTypeMutation = {
  __typename: "MyType";
  id: string;
  title: string;
  content: string;
  price: number | null;
  rating: number | null;
};

export type DeleteMyTypeMutation = {
  __typename: "MyType";
  id: string;
  title: string;
  content: string;
  price: number | null;
  rating: number | null;
};

export type GetMyTypeQuery = {
  __typename: "MyType";
  id: string;
  title: string;
  content: string;
  price: number | null;
  rating: number | null;
};

export type ListMyTypesQuery = {
  __typename: "ModelMyTypeConnection";
  items: Array<{
    __typename: "MyType";
    id: string;
    title: string;
    content: string;
    price: number | null;
    rating: number | null;
  } | null> | null;
  nextToken: string | null;
};

export type OnCreateMyTypeSubscription = {
  __typename: "MyType";
  id: string;
  title: string;
  content: string;
  price: number | null;
  rating: number | null;
};

export type OnUpdateMyTypeSubscription = {
  __typename: "MyType";
  id: string;
  title: string;
  content: string;
  price: number | null;
  rating: number | null;
};

export type OnDeleteMyTypeSubscription = {
  __typename: "MyType";
  id: string;
  title: string;
  content: string;
  price: number | null;
  rating: number | null;
};

@Injectable({
  providedIn: "root"
})
export class APIService {
  async CreateMyType(
    input: CreateMyTypeInput,
    condition?: ModelMyTypeConditionInput
  ): Promise<CreateMyTypeMutation> {
    const statement = `mutation CreateMyType($input: CreateMyTypeInput!, $condition: ModelMyTypeConditionInput) {
        createMyType(input: $input, condition: $condition) {
          __typename
          id
          title
          content
          price
          rating
        }
      }`;
    const gqlAPIServiceArguments: any = {
      input
    };
    if (condition) {
      gqlAPIServiceArguments.condition = condition;
    }
    const response = (await API.graphql(
      graphqlOperation(statement, gqlAPIServiceArguments)
    )) as any;
    return <CreateMyTypeMutation>response.data.createMyType;
  }
  async UpdateMyType(
    input: UpdateMyTypeInput,
    condition?: ModelMyTypeConditionInput
  ): Promise<UpdateMyTypeMutation> {
    const statement = `mutation UpdateMyType($input: UpdateMyTypeInput!, $condition: ModelMyTypeConditionInput) {
        updateMyType(input: $input, condition: $condition) {
          __typename
          id
          title
          content
          price
          rating
        }
      }`;
    const gqlAPIServiceArguments: any = {
      input
    };
    if (condition) {
      gqlAPIServiceArguments.condition = condition;
    }
    const response = (await API.graphql(
      graphqlOperation(statement, gqlAPIServiceArguments)
    )) as any;
    return <UpdateMyTypeMutation>response.data.updateMyType;
  }
  async DeleteMyType(
    input: DeleteMyTypeInput,
    condition?: ModelMyTypeConditionInput
  ): Promise<DeleteMyTypeMutation> {
    const statement = `mutation DeleteMyType($input: DeleteMyTypeInput!, $condition: ModelMyTypeConditionInput) {
        deleteMyType(input: $input, condition: $condition) {
          __typename
          id
          title
          content
          price
          rating
        }
      }`;
    const gqlAPIServiceArguments: any = {
      input
    };
    if (condition) {
      gqlAPIServiceArguments.condition = condition;
    }
    const response = (await API.graphql(
      graphqlOperation(statement, gqlAPIServiceArguments)
    )) as any;
    return <DeleteMyTypeMutation>response.data.deleteMyType;
  }
  async GetMyType(id: string): Promise<GetMyTypeQuery> {
    const statement = `query GetMyType($id: ID!) {
        getMyType(id: $id) {
          __typename
          id
          title
          content
          price
          rating
        }
      }`;
    const gqlAPIServiceArguments: any = {
      id
    };
    const response = (await API.graphql(
      graphqlOperation(statement, gqlAPIServiceArguments)
    )) as any;
    return <GetMyTypeQuery>response.data.getMyType;
  }
  async ListMyTypes(
    filter?: ModelMyTypeFilterInput,
    limit?: number,
    nextToken?: string
  ): Promise<ListMyTypesQuery> {
    const statement = `query ListMyTypes($filter: ModelMyTypeFilterInput, $limit: Int, $nextToken: String) {
        listMyTypes(filter: $filter, limit: $limit, nextToken: $nextToken) {
          __typename
          items {
            __typename
            id
            title
            content
            price
            rating
          }
          nextToken
        }
      }`;
    const gqlAPIServiceArguments: any = {};
    if (filter) {
      gqlAPIServiceArguments.filter = filter;
    }
    if (limit) {
      gqlAPIServiceArguments.limit = limit;
    }
    if (nextToken) {
      gqlAPIServiceArguments.nextToken = nextToken;
    }
    const response = (await API.graphql(
      graphqlOperation(statement, gqlAPIServiceArguments)
    )) as any;
    return <ListMyTypesQuery>response.data.listMyTypes;
  }
  OnCreateMyTypeListener: Observable<OnCreateMyTypeSubscription> = API.graphql(
    graphqlOperation(
      `subscription OnCreateMyType {
        onCreateMyType {
          __typename
          id
          title
          content
          price
          rating
        }
      }`
    )
  ) as Observable<OnCreateMyTypeSubscription>;

  OnUpdateMyTypeListener: Observable<OnUpdateMyTypeSubscription> = API.graphql(
    graphqlOperation(
      `subscription OnUpdateMyType {
        onUpdateMyType {
          __typename
          id
          title
          content
          price
          rating
        }
      }`
    )
  ) as Observable<OnUpdateMyTypeSubscription>;

  OnDeleteMyTypeListener: Observable<OnDeleteMyTypeSubscription> = API.graphql(
    graphqlOperation(
      `subscription OnDeleteMyType {
        onDeleteMyType {
          __typename
          id
          title
          content
          price
          rating
        }
      }`
    )
  ) as Observable<OnDeleteMyTypeSubscription>;
}
